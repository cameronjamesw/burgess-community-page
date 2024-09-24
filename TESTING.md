# Burgess Community Page - Testing

![A photo of the Burgess Community Page being displayed on AmiResponsive](/documentation/images/amiresponsive.png)

Live site can be viewed here - [Burgess Community Page](https://burgess-community-22799d4a8274.herokuapp.com/)

# Contents

* [Introduction](#introduction)
* [Manual Testing](#manual-testing)
* [User](#user)
* [Bugs](#bugs)
* [Lighthouse](#lighthouse)
* [Validation Testing](#validation-testing)
    * [HTML](#html)
    * [CSS](#css)
* [Python Testing](#python-testing)

# Introduction

Throughout the process of creating the Burgess Community Page, I have been conducting tests within each section and function/model. I have mainly been testing for functionality and styling issues, whilst keeping an open eye for any other issues that may pop up. Along with myself performing manual tests, I have also had an array of users, family and friends, testing the website for optimal functionality.

# Manual Testing

In any instance of a fail there is a detailed description and resolution underneath!

### Admin Testing

| Test | Outcome | Pass or Fail
| --- | --- | --- |
| Create Discussion | A successful discussion was created, and was displayed as unapproved to the author, upon approval it was displayed for other users. When displayed though, the discussion content is displayd in HTML code(*). | Fail |
| Edit Discussion | A pre-existing discussion was edited within the admin panel and successfully updated on the discussion page. However, as noted above, the content appears to be in HTML(*). | Fail |
| Approve User Discussion | Discussion appears  for all users within feed upon approval, is not there otherwise | Pass |
| Approve User Comments | Comments appear for all users under relevent discussion when approved | Pass
| Delete User Comments | Comments successfully deleted | Pass |
| Delete Discussions | Successfully deleted discussions | Pass |
| Create Staff Profile | Staff Profile successfully created | Pass |
| Delete Staff Profile | Staff Profile successfully deleted | Pass |
| Delete User | User successfully deleted, along with profile, discussions and exisitng comments | Pass |

(*) - When creating discussions within the admin panel, the content when parsed through to the template appears to be in HTML code, instead of humanly readable content. (see below)
![A screenshot of the HTML error referenced above](documentation/images/html_error.png)

# User

# Bugs

- The first bug that I have encountered is within the authentication process. The user is required to sign up with an email, and in doing so an email verification link is sent to the email in question. However, no link is being sent to the user. The current work around that I have for this is that the link for verify the email is being sent to the console, and it is acessissible that way. I have also altered the verification settings so that the user does not need to have their email verified in order for them to log in. 

# Lighthouse

# Validation Testing

## HTML

## CSS

# Python Testing
