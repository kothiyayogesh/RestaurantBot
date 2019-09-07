Also read this in-depth information about NLU here: https://blog.rasa.com/rasa-nlu-in-depth-part-1-intent-classification/ 

Core policy
Till now we saw how chatbot understands the user sentence and classifies to proper intent and extract entities. 
But we humans follow natural conversation where we remember context and reply accordingly. Otherwise, it will look something like this. Frustrating 😠 isn't it?

So how does rasa handles all this? It is done through various elements of the RASA. Let’s look at the architecture of the RASA.

Here Interpreter is part of NLU and Tracker, policy and action are part of Core.
* The message is passed to an Interpreter, which converts it into a dictionary including the original text, the intent, and any entities that were found.
* The Tracker is the object which keeps track of the conversation state. It receives the info that a new message has come in. Know more about it here: https://rasa.com/docs/rasa/api/tracker-stores/
* The policy receives the current state of the tracker, chooses the next action which is logged by the tracker and response is sent to the user. There are different policies to choose from.   
You will get more information here: https://rasa.com/docs/rasa/core/policies/#policies  
Along with policy “slots” which act as bot’s memory(context). It also influences how the dialogue progresses. Read more about slots here: https://rasa.com/docs/rasa/core/slots/

These settings are part of config.yml (Think this file as the brain of chatbot :P)

So far so good? We have gone through the psychology of the bot. Now it’s time to look at the environment of the chatbot which will help it to learn. 
Just like a growing baby, he/she learn from whatever is experienced. Similarly will need to train a chatbot with right training data.   
Which comes in the form of text utterances part of defined intent with the tagged entity for training NLU and as a story(like a conversation) to train RASA core.   
Read more about training data for NLU here: https://rasa.com/docs/rasa/nlu/training-data-format/ and for stories here: https://rasa.com/docs/rasa/core/stories/

As planned before we need to be very thorough with the scope of the bot. Hence we need to define its own universe in which our bot operates. It has the intents which it should classify to, entities which it should extract, slots which it should remember to maintain context, and actions which it should perform to complete the task. And response templates which bot should utter back. Read more about domain file here: https://rasa.com/docs/rasa/core/domains/
> Actions are the things your bot runs in response to user input.  
Read more about actions here: https://rasa.com/docs/rasa/core/actions/

Now we have all the ingredients ready to build a chatbot.
* Defining the scope of the bot ✅
* Exploring Zomato API ✅
* Understand RASA and its components ✅

Now let’s set up and develop

#### Setup and installation instructions:

* Download and install anaconda: https://docs.anaconda.com/anaconda/install/ 
* Create a conda virtual environment: https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/
* Install RASA : https://rasa.com/docs/rasa/user-guide/installation/#quick-installation
and other missing dependency(spacy) : https://rasa.com/docs/rasa/user-guide/installation/#dependencies-for-spacy

Go through this quick RASA tutorial: https://rasa.com/docs/rasa/user-guide/rasa-tutorial/ for quick setup.

Now let’s add missing spices one by one to completely prepare the delicious dish.  
1. Understand the chatbot’s conversation flow again and create an NLU and story training data based on that.
  Few pointers: 
  * Assume that you are the first user who is talking to the bot and thinks of all-natural and quirky conversation you can have :P and prepare NLU and stories training data.
Don’t forget to include small talk(greetings, deny etc) in the training data.
Keep the all intents mutually exclusive and diversity in its utterance.
	> Note: No need to have comprehensive training data because we are going to explore rasa x to do the same in a much more comfortable way.

* Set appropriate NLU pipeline and policy configuration.
> For NLU we will use the English language and default spacy pipeline (pretrained_embeddings_spacy).
> For Core, we will use MemoizationPolicy and KerasPolicy. As it’s ML-based bot. Explore other ways to build the bot.
* Write a domain.yml file.
* Write an action.py file - action.py file is self-explanatory as all classes and functions are well commented.
* Write an endpoint.yml file - this file contains the different endpoints which your bot can connect to. Like tracker store, events, actions, etc.

Now it’s time to train the bot. 
Execute below command and explore this for more training options: https://rasa.com/docs/rasa/user-guide/command-line-interface/#train-a-model
`rasa train`
Let’s see how bot performs with limited training data and let’s explore rasa x and improve it.
Run the following command in every new tab.
`rasa run actions`
`rasa x`
Open rasa x for testing and improving the story through interactive learning. Check [Juste's video intro to Rasa X](https://www.youtube.com/watch?v=VXvWdrr2yw8&feature=youtu.be) for more information.

