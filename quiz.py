import json

class Quiz:
    def __init__(self):
        self.points = 0
        self.rightAnswerNumber = 0

    def initialize(self):
        questionObjects = self.readFromFileQuestions()
        for questionObject in questionObjects:
            self.printQuestionAndAnvaiableAnswers(questionObject)
            self.resolveRightAnswearValue(questionObject['answers'])

            maxAnswerValue = len(questionObject['answers'])
            self.resolveAnswear(maxAnswerValue)

        self.calculateStatistics()

    def printQuestionAndAnvaiableAnswers(self, questionObject):
        print(questionObject['question'])
        for answerOption in questionObject['answers']:
            print(answerOption['name'])

    def readFromFileQuestions(self):
        with open('quizQuestions.json') as json_file:
            return json.load(json_file)

    def resolveRightAnswearValue(self, answerCollection):
        rightAnswerIndex = 1

        for answer in answerCollection:
            if answer['value'] == True:
                self.rightAnswerNumber = rightAnswerIndex
            rightAnswerIndex += 1

    def resolveAnswear(self, maxAnswerValue):
        inputQuestion = 'Podaj odpowiedź z zakresu 1 do ' + str(maxAnswerValue) + ': '

        while True:
            answerValue = int(input(inputQuestion))
            if 1 <= answerValue <= maxAnswerValue:
                if self.rightAnswerNumber == answerValue:
                    self.points += 1

                break

    def calculateStatistics(self):
        print("Twój wynik to: " + str(self.points) + ' punktów.')

quizObject = Quiz()
quizObject.initialize()
