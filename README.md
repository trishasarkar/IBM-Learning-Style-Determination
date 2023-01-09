# Learning Style Determination (by IBM)

## Project Phase:

* This project was completed in 2 phases: Phase I by [Anirudh Ambati](https://github.com/anirudhambati), after which it was handed over to [Trisha Sarkar](https://github.com/trishasarkar) to complete Phase II

##  Phase II -

### Problem Statement:

Create a learning style determination system which can help to understand the learning style of a user as per the VAK Model of learning. The system computes the learning style based on the user input and can also be confirmed using the eye movements captured using an electrooculography (EOG) device.

### Application:
Our country uses the age-old ROTE method for delivering student lectures and not much significance is given to learning disabilities or slow learning. If the content is created which is aligned to their learning style, learning is much more effective and faster. At present, none of the learning platforms provides content aligned to Audio or Kinesthetic as it's mostly Visual. Users who are not Visual, find it difficult to learn it effectively and are categorized as slow learners which impacts their overall physic. Our system will help user to determine his/her preferred learning styles using multi-modal learning thru eye movement and user response.

### Responsibilities:
  ❖ Front-end (use of HTML, CSS and JavaScript): Redesign the UI and the sliders.
  ❖ Machine Learning: Create a model for prediction
  ❖ Integrate the model to the website, such that the website displays both the results.
  
### Demystification:

A detailed account of the work done in Phase II, as submitted to IBM can be found [here](https://drive.google.com/file/d/1sG_DAa8-muY5gjSO3CO8XeBlIy0zNAaD/view?usp=sharing).

## Phase I -

* Documentation:

  1. home is the main app
  2. Static in the main repository has been used to gather static files while hosting
  3. Db is IBM cloudant. npm json bin has been used for data. get_data() function in home/views.py gets the questions and options data from npm api.
  4. choose_category() in home/views.py return the html code for the choose category page. This code will be attached to the global template and gets rendered.
  5. Input checkboxes for each category of data available must be created here. for ex: if we have to add 2 new categories, we need to add 2 new input fields with the category names here.
  6.  Similarly scene dictionary in get_scene() (in 'home/views.py') must be added for every category to be added/modified.
  7. quiz function in 'home/views.py' asks to chose category and shows the screen of the first scenario.
  8. quiz2 is the main loader for the quiz part. all questions and options are displayed from this view.
  9. by default this view stores the responses of previous question AND gets the session info of scenario.no and question.no and shows the next scenario/questions
  10. if there is some 'action' (jump section/exit), then it takes actions accordingly
