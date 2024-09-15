# Burgess Community Page

Picture of the finished project


Live site can be viewed here - link

# Contents

* [Introduction](#introduction)
* [Project](#project)
    * [Site Objectives](#site-objectives)
* [User Experience / UX](#user-experienceux)
    * [Target Audience](#target-audience)
    * [User Stories](#user-stories)
        * [New Visitor Goals](#new-visitor-goals)
        * [Existing Visitor Goals](#existing-visitor-goals)
* [Design Choice](#design-choice)
    * [Typography](#typography)
    * [Color Scheme](#color-scheme)
    * [Logo & Favicon](#logo--favicon)
    * [Wireframes](#wireframes)
    * [Flow Diagram](#flow-diagram)
    * [Database Plan](#database-plan)
* [Features](#features)
    * [Sign Up / Registration](#sign-up--registration)
    * [Creating a Discussion](#creating-a-discussion)
    * [Commenting on a Discussion](#commenting-on-a-discussion)
    * [Profile Customisation](#profile-customisation)
    * [Future Features](#future-features)
* [Technologies Used](#technologies-used)
* [Programming Languages, Frameworks & Libraries Used](#programming-languages-libraries--frameworks-used)
* [Agile](#agile)
* [Testing](#testing)
* [Deployment](#deployment)
    * [Github Deployment](#github-deployment)
    * [Creating a Fork or Copying](#creating-a-fork-or-copying)
    * [Clone](#clone)
    * [Repository Deployment via Heroku](#repository-deployment-via-heroku)
    * [Deployment of the App](#deployment-of-the-app)
* [Credits](#credits)
* [Media](#media)
* [Acknowledgements & Thanks](#acknowledgements--thanks)

# Introduction

Welcome to the Burgess Community Page, a website designed to be used by the staff of Camp Burgess in Sandwich, Massachussetts. 

Camp Burgess is an overnight summer camp based in Cape Cod, Massachusetts. The camp was founded in 1928 by the South Shore YMCA and since the 60s has had an influx of international staff working there, with staff being hired from all over the world.

![An image of Cape Cod, Massachussetts](documentation/images/cape_cod_image.jpg)

The Burgess Community Page is a website which is designed to give staff members, old and new, a platform to communicate within a grander scale. Staff members are able to create discussions within the community website where they can discussion fond memories and ongoing experiences that all relate to working at Camp Burgess.

# Project

## Site Objectives

The objectives of the Burgess Community Page are as follows..

- ### Create clean, readable front-end code that is accessible and easily navigated by users.

I aim to create a website with not only flare and accessibility, but a website that has a unique User Interface through the use of both Bootstrap and Django. 

- ### Make use of available back-end functionality

Through the use of backend frameworks, the user will be able to create their own profile within the Burgess Community where they can customise to their liking. Furthermore, upon authentication, the user will be able to create and edit their own discussion posts, as well as leave comments on other discuussion too. 

- ### Store data on an external cloud database

I will be using ElephantSQL to store the PostgreSQL database for this project.

# User Experience/UX

## Target Audience

- The target audience for the Burgess Community Page will be staff members, current and old, who are interested in sharing their experiences and memories with other like-minded individuals.

- Ideally the website will attract the attention of future staff members that share similar goals and interests to the current staff. In turn, this will encourage the Burgess Staff community to grow and raise awareness of the opportunity to work abroad for interested individuals. 

## User Stories

### New Visitor Goals

- Gauge an understanding of what Camp Burgess is along with creating an understanding of summer camp culture.
- Successfully navigate around the site and read discussions from existing members.
- Create their own account and profile as well as engage with other site users.

### Existing Visitor Goals

- Log in and out of their account.
- Interact with new and exisitng users.
- Customise and update their profile page to give a sense of individuality within the website.
- Create and edit comments on other users' discussions.

# Design Choice

In this section the different design choices will be explained along with their thought-process.

## Typography

The main font style that I have used is 'Teko' from [Google Fonts](https://fonts.google.com/specimen/Teko). Teko has been used for the heading tags throughout the project. The typography of Teko fits the purpose of the project as the font-style is definitive and noisy, and in my opinion it reinforces the sleek flare insinuated by the website.

## Color Scheme

![An image of the color scheme used throughout the webiste](documentation/images/BCP%20Color%20Pallet.png)

The color scheme that I have used is one that I feel best represents the camp culture, and one that I feel creates excellent synergy throughout the entire website. 

- It is no suprise that I have used both `#ffffff` and `#000000` as I feel that these two base colors create a nutricious foundation for any potential color scheme to build upon. I am a big fan of using both black and white as they are so minimalist and I feel that there is a much greater attention to detail with these two colors.

- I used `#d3d3d3` as an emphasis color to add to `#000000` and really make certain features stand out and bring attention to something. For example, any text boxes or hovered links really perform well when using `#d3d3d3` as they provide excellent UX for the user as this sends a message that these areas require your attention.

- I have used `#112a12` as the primary and most consistent color throughout the project. It is featured within both the header and footer of the project, along with any important submit buttons. The thought behind this is that it is a sleek, rich color that will add flare to the website, but more importantly it is a classic camp color which provokes a rural, natursitic feel within the user. 

- Finally, I have used `#CD5909` as a base secondary color. This color is elicited within a majority of the images throughout the website and it provides a completementary viewpoint to `#112a12`.

## Logo & Favicon

- The logo used was provided by Camp Burgess and Hayward.

- The Favicon used was a cartoon campfire found over at [Vector Stock](https://www.vectorstock.com/royalty-free-vector/campfire-vector-917478). 

## Wireframes

## Flow Diagram

## Database Plan

# Features

## Sign Up / Registration

## Creating a Discussion

## Commenting on a Discussion

## Profile Customisation

## Future Features

# Technologies Used

# Programming Languages, Libraries & Frameworks Used

# Agile

# Testing

The testing file for the Burgess Community Page can be viewed [here](/TESTING.md)

# Deployment

## GitHub Deployment

The website was stored using GitHub for storage of data and version control. To do this I did the following;

After each addition, change or removal of code, in the terminal within your IDE (I used GitPod for this project) type:

- git add .
- git commit -m "meaningful and succinct commit message"
- git push

The files are now available to view within your github repository.

## Creating a Fork or Copying

To clone/fork/copy the repository you click on the fork tab which is situated next to unwatch tab in the top right corner of the page when viewing the repository.

## Clone

To create a clone you do the following;

1. Click on the code tab, left of the Gitpod tab
2. To the right of the repository name, click the clipboard icon
3. In the IED open GitBash
4. Change the working directory to the location you prefer
5. Add Git Clone with the copy of the repository name
6. Clone has been created

## Repository Deployment via Heroku

- On the Heroku Dashboard page, click New and then select Create New App from the drop-down menu.
- When the next page loads insert the App name and Choose a region. Then click 'Create app'
- In the settings tab click on Reveal Config Vars and add the key Port and the value 8000. The credentials for this app were:
    - Cloudinary URL
    - Postgres Database URL
    - Port (8000)
    - Secret Key (unique to you)

- Below this click Add buildpack and choose python and nodejs in that order.

## Deployment of the App

- Click on the Deploy tab and select Github-Connect to Github.
- Enter the repository name and click Search.
- Choose the repository that holds the correct files and click Connect.
- A choice is offered between manual or automatic deployment whereby the app is updated when changes are pushed to GitHub.
- Once the deployment method has been chosen the app will be built and can be launched by clicking the Open app button which should appear below the build information window, alternatively, there is another button located in the top right of the page.

# Credits

# Media

- [Vector Stock](https://www.vectorstock.com/royalty-free-vector/campfire-vector-917478) - The Favicon was taken from Vector Stock

- [Flickr](https://www.vectorstock.com/royalty-free-vector/campfire-vector-917478) - The Cape Cod image was taken from Flickr

# Acknowledgements & Thanks