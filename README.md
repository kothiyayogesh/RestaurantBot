### Chatbot

The popularity of live chat applications has been growing over the past few years. And as the AI trend keeps rising, chatbots become more a must-have rather than a nice to have part of the business. The increasing demand for chats continues to grow so to keep the customer satisfaction rate high; companies must find ways to cope with the rising volumes of inquiries coming every day to all their communication channels.

Chatbots have no competition when it comes to turnout and motivation. They never get tired, bored or distracted.

Google 2018 I/O heated up the topic showing their Duplex AI-powered assistant that smoothly managed to book a table, and schedule appointments speaking with humans. The presentation blew everyone’s mind! 

> __Chatbots are getting - smarter, more accessible and useful.__

### Various types of bots

[Conversational AI: Your Guide to Five Levels of AI Assistants in Enterprise](https://blog.rasa.com/conversational-ai-your-guide-to-five-levels-of-ai-assistants-in-enterprise/)

### Bot building platforms and frameworks

> _list is long and coming soon_

### The Architecture of chatbot 

![https://chatbotsmagazine.com/the-ultimate-guide-to-designing-a-chatbot-tech-stack-333eceb431da](https://miro.medium.com/max/1078/1*BVBQ-uiAOYB9LthbSoiUUA.png "Logo Title Text 1")

Read more about [here](https://blog.vsoftconsulting.com/blog/understanding-the-architecture-of-conversational-chatbot)

The awesomeness about **Co-learning lounge** is we explore everything in detail 😍 Here also we will go from project selection, design/documentation, development to deployment of the bot.

### Project selection  
This definition however often leads to two potential misconceptions.
The biggest misconception that arises is that a chatbot is a bot that converses with a human in the way that another human would converse with a human. Software or even a robot (the digital part of the robot is of course software) that communicates with a human in natural language is not difficult to imagine. Science fiction is full of examples.

While this may be the end goal, this is simply not possible using the current technology. Not only is it not possible, it often leads to unrealistic expectations regarding the chatbot's capabilities and inevitable frustrations when those expectations are not met.

The second misconception is that a chatbot communicates using only text or voice. Actually, chatbots allow users to interact with them via graphical interfaces or graphical widgets, and the trend is in this direction. Many chat platforms including WeChat, Facebook Messenger and Kik allow web views on which developers can create completely customized graphical interfaces.

Chatbots can be used in many different ways, which is the reason why it’s difficult to define exactly what they are. It is actually possible to come up with a chatbot use case for every single business or industry, in the same way, that every business or industry can use a website or app.	
Literally any task you can do delegate to Chatbot. A couple of things you can definitely do is training chatbot to handle FAQs, Basic flow handling where it can help the user to view,  purchase, or track something, feedback collection or notification. 

All the above examples of chatbots could allow human agents to get involved in the conversation if necessary, perhaps as a premium service.

### Documentation/Design

Detailed conversation design based on a defined scope is the first thing you should do before you head to development. If you are completely new to it and don’t know where to start then we recommend this article: [How to design a robust chatbot interaction](https://uxdesign.cc/how-to-design-a-robust-chatbot-interaction-8bb6dfae34fb?gi=b521852a15a6)

Just like human chatbot needs to have personality, persona, and tone too(Aren't chatbot supposed to behave like a human 😜) Read more about chatbot personality here : [Why AI And Chatbots Need Personality](https://www.linkedin.com/pulse/why-ai-chatbots-need-personality-bernard-marr/?trackingId=if7XdV00TsqtxL0WwiJfAw%3D%3D)

There are a couple of online tools you can use to layout chatbot's conversation design.  
[moqups](https://moqups.com/)  
[draw.io](https://www.draw.io/)

Read this thread to find out more apps/software: https://news.chatbotsmagazine.com/t/tool-method-to-design-conversation-diagram/915/20

In this tutorial, we will build a simple to complex restaurant bot step by step with the objective of exploring all awesome features of RASA and make a personal assistant for yourself or for your business. 
We assume you have gone through the chatbot introduction,  various types of the chatbot, how to select chatbot as a project, It’s design practice, etc. 
If not then we highly recommend that you read the README of this section.

In this phase, we will be building a simple flow where users can search restaurants on bot through Zomato API based location and cuisine. 
As per the best design practice, the bot should welcome the user with the greeting and let the user know what bot can do. 
If user request matches with in-flow intents and if there are no or missing entities in the utterance then bot should ask required entities (cuisine and location in this phase) to complete the action (search restaurant from Zomato API). 
Here will train our model to extract cuisine and will use Bing map API to extract location as it’s impossible to train every damn location. 

To hit Zomato API with location we need entity_id, entity_type, lat and long which will get from [/location](https://developers.zomato.com/documentation#!/location/locations) and for cuisine, we need cuisine_id which you will get from [/cuisines](https://developers.zomato.com/documentation#!/common/cuisines)
Once we have all the details we can hit [/search](https://developers.zomato.com/documentation#!/restaurant/search) which is the main and final endpoint where you will get restaurant details. By default, you will get 20 top matched restaurants. We kept count as 5. Play around with Zomato API to get comfortable with it: https://developers.zomato.com/documentation

#### Zomato API
To start with, we will need an API key from Zomato, so navigate to [Zomato](https://developers.zomato.com/api) and ‘request an API key’.  
On being prompted, we may either sign up on Zomato or ‘Continue with Google’. After we have completed the sign up, we should receive the API key

#### Microsoft Bing Maps REST API
To use the Bing Maps REST API, we will need ‘Bing Maps Key’. Therefore, navigate [here](https://docs.microsoft.com/en-us/bingmaps/getting-started/bing-maps-dev-center-help/getting-a-bing-maps-key) and then click on ‘Bing Maps Key’ hyperlink. After we have signed up (if we do not have an account on Microsoft) and provided our basic information, we can create a key. Bing Maps API provides a ‘basic’ key, by default (i.e. it can be specified directly in the request header, no need of OAuth complexity).  
After the key has been created we can see/ copy it by clicking on ‘My Account’ -> ‘My Keys’.  
Now, we have what we needed to start with. Let’s dive in to Postman and get the stuff working.

Look at the below self-explanatory state diagram which shows conversation flow with all required states.

### What is Rasa?
[Rasa](https://rasa.com/docs/rasa/) is an open-source machine learning framework for building [contextual AI assistants and chatbots](https://blog.rasa.com/level-3-contextual-assistants-beyond-answering-simple-questions/).  
To make complete AI-based chatbot it has to handle two things: 

* Understanding the user’s message which is done through Rasa [NLU](https://rasa.com/docs/rasa/nlu/about/).
* The bot should be able to carry dialogue with context which is done by Rasa [Core](https://rasa.com/docs/rasa/core/about/).

Rasa’s document is very intuitive so in this tutorial, I will direct to appropriate section of the document.

### Skeleton of Rasa
Since hype was to match chatbot with humans. We will take the human analogy to understand the components of the chatbot. 

#### Bot configuration
Firstly we will understand the body parts of the human(mostly brain, Don’t worry it’s not biology class) which we call “Bot configuration” in the bot world. 

Primary thing we humans do is communicate. And language is the primary means of communication. So for the bot as well we need to set language. We will use the English language for the bot. But you can build a multi-lingual bot with RASA.  
For more information about languages supported by rasa refer: https://rasa.com/docs/rasa/nlu/language-support/

Now put on your apron and get ready with a scalpel to see what’s in the brain 😃. Seems like it’s way complex. Chuck it, but the point is whenever we hear something we process the information through millions of neurons to understand the meaning of the sentence with its context, etc. And our brain is smart enough to generate a proper response based on a question. So are we going to build that intelligent bot?. Hold on! We can but not right now. The best way to think and start building a chatbot is like a newborn baby. It learns with experience :) Now let’s understand how the brain of chatbot works. It’s called NLU(Natural language understanding) unit where it’s components do the job. Component includes as follows.

1. Tokenization: 
We read and understand the sentence word by word, right? Similarly, tokenizer will break the sentence into words(called word tokenizer).   
For more information on RASA supported tokenizer refer: https://rasa.com/docs/rasa/nlu/components/#tokenizers

2.  Featurizer: 
We infer meaning by words and when all words are combined in a sentence then we infer the meaning of the sentence with context, right? Similarly, tokenized words are used as features to the post components of the pipeline. These features are has meaning of the word(mathematically) which is called Embeddings. Get to know more about word embedding here. Embedding comes in below two flavors.   
    ###### Embedding:  
	1. Pre-trained:   
Here word embeddings are already trained on huge text datasets with various state-of-the-art architecture. Popular word embeddings are XLNet, BERT, Glove, etc. We can use word embedding as it is in our NLP pipeline when we don’t have much training data. This technique is called as transfer learning.  
	2. From scratch:   
When pre-trained does not work well because it might have trained on your domain-specific then we can train our own word embedding from scratch. It is recommended when you have sufficient training samples.   
RASA supports both types of word embedding. Refer this for more: https://rasa.com/docs/rasa/nlu/choosing-a-pipeline/#a-longer-answer  
For more information on RASA supported featurizers refer:  https://rasa.com/docs/rasa/nlu/components/#featurizers    
     3. Count vectorizer:  
       You can convert a sentence into features using a bag of words. Where you can have unigram, bi-gram, tri-gram.   
Check this for more information: https://rasa.com/docs/rasa/nlu/components/#countvectorsfeaturizer  
> Another interesting tweak is to increase the number of n-grams, which is 1 by default. By using a max_ngram of 2, you will create additional features for each couple of consecutive words. For example, if you want to recognize “I'm happy” and “I'm not happy” as different intents, it helps to have not happy as a feature.

3. Entity extraction   
These are a chunk of information we extract from sentences to complete the action. For example when we say `I want to travel from Hyderabad to Mumbai by flight`. Here the intent is “travel_flight" and to fetch information we need to know source i.e Hyderabad and destination i.e Mumbai and couple more entities like date of travel etc.

Once the intent is identified and all entity is extracted then we can complete the action by calling the required API.

Read more about entity extraction here: https://rasa.com/docs/rasa/nlu/entity-extraction/
 
4. Classifier  
Now you know the meaning(features) of the sentence(words through tokenization). It’s time to classify to its appropriate category. For e.g `I want to travel by cab` should classify to travel_cab and `I want to travel by flight` travel_flight. All this is done by using Machine learning or Deep learning classifier.  
Read more about supported RASA classifier here: https://rasa.com/docs/rasa/nlu/components/#intent-classifiers  
For more information about NLU pipeline and it’s component refer: https://rasa.com/docs/rasa/nlu/choosing-a-pipeline/ & https://rasa.com/docs/rasa/nlu/components/

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
