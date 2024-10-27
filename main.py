''' 
welcome users to our quiz
store a list of questions that we will later ask the user
keep track of points
go through the questions in the list
  ask the user each question and lets store their response
  depending on their response we increment points
  depending on how many points the user has we display a different     message 
'''

print ("welcome to the quiz: how much do you know about india?")
questions = ["what is the capital of india?", 
             "who is the father of the indian nation?",
             "what is the national animal of india?", 
             "what is the national fruit of india?" ,
             "what is the national tree of india?" ]
points = 0

for question in questions:
  response = input(question + " ")
  if response.lower() == "new delhi":
   points = points +1
   print(points)
  elif response.lower() == "delhi":
     points = points +1
     print(points)
  elif response.lower() == "delhi ncr":
   points = points +1
   print(points)
  elif response.lower() == "gandhi":
   points = points +1
   print(points)
  elif response.lower() == "mahatma gandhi":
   points = points +1
   print(points)
  elif response.lower() == "mk gandhi":
   points = points +1
   print(points)
  elif response.lower() == "gandhiji":
   points = points +1
   print(points)
  elif response.lower() == "tiger":
   points = points +1
   print(points)
  elif response.lower() == "bengal tiger":
   points = points +1
   print(points)
  elif response.lower() == "mango":
   points = points +1
   print(points)
  elif response.lower() == "banyan":
   points = points +1
  elif response.lower() == "banyan tree":
   points = points +1
   print(points)


if points == 0 :
  print("you dont know too much about india")
if points == 1 :
  print("you dont know too much about india")
if points == 2 :
  print("you dont know just a little")
if points == 3 :
  print("you dont know enough to fit in")
if points == 4 :
  print("you know almost everything there is to know")
if points == 5 :
  print("genius! you know everything there is to know about india")