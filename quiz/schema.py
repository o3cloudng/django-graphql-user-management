import graphene

from graphene_django import DjangoObjectType
from graphene_django import DjangoListField

from .models import Quizes, Question, Category, Answer


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = "__all__"


class QuizType(DjangoObjectType):
    class Meta:
        model = Quizes
        fields = "__all__"


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = "__all__"


class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = "__all__"

class Query(graphene.ObjectType):
    all_quizzes = DjangoListField(QuizType)
    single_quiz = graphene.Field(QuizType, id=graphene.Int())

    def resolve_single_quiz(root, info, id):
        return Quizes.objects.get(pk=id)
    
    all_questions = DjangoListField(QuestionType)
    single_question = graphene.Field(QuestionType, id=graphene.Int())
    def resolve_single_question(root, info, id):
        return Question.objects.get(pk=id)
    
    all_answers_to_question = graphene.List(AnswerType, id=graphene.Int())
    def resolve_all_answers_to_question(root, info, id):
        return Answer.objects.filter(question=id)
    
    all_categories = DjangoListField(CategoryType)
    single_category = graphene.Field(CategoryType, id=graphene.Int())
    def resolve_single_category(root, info, id):
        return Category.objects.get(pk=id)


##############      MUTATIONS
### ADD CATEGORY
class CategoryMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, name):
        category = Category(name=name)
        category.save()
        return CategoryMutation(category=category)

### UPDATE CATEGORY
class CategoryUpdateMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String(required=True)

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, name, id):
        category = Category.objects.get(id=id)
        category.name = name
        category.save()
        return CategoryMutation(category=category)


class CategoryDeleteMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, id):
        category = Category.objects.get(id=id)
        category.delete()
        return "Deleted successfully."


class Mutation(graphene.ObjectType):
    add_category = CategoryMutation.Field()
    update_category = CategoryUpdateMutation.Field()
    delete_category = CategoryDeleteMutation.Field()




schema = graphene.Schema(query=Query, mutation=Mutation)