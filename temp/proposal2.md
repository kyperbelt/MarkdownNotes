---
title: CSC190 Project Proposal | Adapted Strength Web App
author: Jonathan Camarena Camacho | jcamarenacamacho@csus.edu
instructor: Kenneth Elliot | kenneth.elliott@csus.edu
client: 
---

# CSC190 Project Proposal | Adapted Strength Web App

## Client Information

Alex-Andre B. Palting | alexandre.palting@adaptedstrength.com | (707)-290-4898

## Problem
The client is a coach at a gym in Vacaville CA that needs a website overhaul. Current website is named Adapted Strength and can found [[here](https://www.adaptedstrength.com/)] and uses various different services to achieve functionality. The client would like to consolidate most functions into a single website/application. 

## Requirements

### Client Requirements
These are the requirements requested by the client. Those prefixed with a `$` are phase 0 requirements. Those prefixed with `+` are possible stretch goals. After speaking with the client (Alex

> :construction: After discussion witht he client, it was mentioned that for convenience and maintainability we could create a single web application that can work across several platforms.

* Website
    - **Home** 
    - **Testimonials**
    - **Mission/About**
        - **Staff/Gym History** 
    - **Meet/Competition Info**
    - **Free Version**: a tab with free/limited access to some content.
    - **Link to App** 
        > :warning: Would consider creating a single webapp that also functions as the mobile appliation. This can address synchronization issues between website and app.
* Application
    - `$` **Sign in/Login**
    - **Scheduling Center**: Deeplink to device calendar.
    - `$` **Chat System**: Communication with coach.
        - mass push notifications. Like announcements from discord.
        - This also has a requirement of letting users upload short clips for trainer to to see.
    - `$` **Movement Library**: Database of videos displaying workouts.
        > :construction: Storage of video examples not necessary. We can use third party service.
    - `$` **Programming Library**: Workout routines for different individuals.
        > :
    - `+` **Profile**: Store user data
        > :construction: Client specified that this is not a requirement, but it could be a good place to manage things like account subscription etc.
        - **BMI**
        - **Height**
        - **Weight**
    - `+` **Nutrition Page**: Calculates client macros.
    - `+` **Resources Page**: Link to nutrition page and supplement and links to purchase. 
        > :information_source: I don't understand this page, but maybe this might be better suited for an above the fold feature rotator?
    - `$` **Leaderboard**: Shows **PR**s of all atheletes/client and improvement over time.
    

### Project 190 Requirements
These are the project 190 requirements and how this project meets those requirements.
* Front end (GUI)
    - Website/App
* Database Backend
    - Storage of videos
    - User Information
    - Subscription Access
* Login/Authentication
    - Users must be authenticated to verify access level.

## Glosary
* **PR**: Personal Record? 
