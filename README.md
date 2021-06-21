Project Requirements
• Create a group composed of 4-5 people from your section. Each individual should only belong to one group.

• Develop a calculator in Python with a graphical user interface (UI).

• The calculator must have the following simple functions:

– Numeric keypad (0-9) with decimal point

– Can perform addition (+) , subtraction (-), multiplication (x), and division (%).

– Your calculator should be capable of chaining multiple operations together and it must execute them in the correct order.

∗ The basic requirements that does not require you to implement parentheses in your operations.

– A delete button that deletes one character at a time

– A clear button that deletes everything that is written on the screen

– You can also include other functionalities that you see fit as long as you fulfill the basic requirements stated above.

• Create a github repository that will host your project. This github repos�itory must be public.

• All members must commit to this repository. Members with no commits will automatically get zero. Wag po tayong pabuhat.

• Setting up your projet should be done in one step only, particulary, by running: pip install -r requirements.txt

• Running your project should also be done in one step only: python main.py

• I also expect that you will be writing tests for the project. I should be able to run these tests using one command only: python test.py

• A 2-3 minute video (by group) that documents what you have done in this project.

GIT
Since we will be using Github, let us take advantage of the optimizations it introduces on our workflow.

• Your project should have a minimum of 3 branches. – The main development branch – Branch for developing the calculator logic.

– Brach for developing the UI. Depending on how you divide the tasks, your repository can have more branches.

• You can use Github’s issues feature to act as a checklist/project management tool. You can create individual issues to signify each feature that you want to implement for the project.

• Add a README.md file in the root directory of your repository.

Dividing Tasks
Let’s assume a group of 4 people. With object oriented-programming, we can easily separate the logic of the calculator from it’s user facing component which is the UI. • One person will act as the team leader. He will manage the github repository, write some unit tests, and be the one in charged with integrating the calculator logic with the UI. Also, this person must be knowledgeable in merging different git branches together.

• The other one will be in charged of writing the calculator logic. He can also participate in writing the unit tests to assure that the calculator logic is working well.

• The third person will be the one assigned in doing the UI. Python has a lot if available packages that can be used in developing UI components. It is the job of this team member to determine what library will best suit this application. He/she can also write some unit tests to assured UI components are behaving as desired.

• The last member will be in charged with the documentation and should be the one in charged in writing the majority of the unit tests.

LETSGOO
