# [ONE BIG DARK ROOM](https://one-big-dark-room-87cda9aa36e7.herokuapp.com)

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/craigdickerson725/one-big-dark-room)](https://github.com/craigdickerson725/one-big-dark-room/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/craigdickerson725/one-big-dark-room)](https://github.com/craigdickerson725/one-big-dark-room/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/craigdickerson725/one-big-dark-room)](https://github.com/craigdickerson725/one-big-dark-room)

Welcome to One Big Dark Room!  This website is designed to help musicians in the goth community connect with band projects near them.  Users who are musicians looking for bands within the 'goth' sub-genres (ie, Darkwave, Post-Punk, Synthwave, Goth Rock, etc) can search the Band Listings (on the Home page) for bands near their location who have open spots.  Likewise, users who have band projects, but not enough musicians to complete their line-up, can create a band listing describing their sound and what instruments they'd like to have added to their band.  My hope is to make it easier for musicians in the goth community to connect with others who can help them fulfill their musical visions, as well as to create a presence in their local music scene.  In the future, I hope to grow the site to add the ability for bands to post their music as well, and to include a section to help bands with booking gigs.

![screenshot](documentation/mockup.png)

source: [amiresponsive](https://ui.dev/amiresponsive?url=https://one-big-dark-room-87cda9aa36e7.herokuapp.com)

## UX

The goal of One Big Dark Room is to provide an intuitive platform where users can easily list and discover band projects. The design and functionality of the application prioritize ease of use, simplicity, and clarity, creating a smooth experience for both band creators and potential collaborators.

### Key Features:

#### Homepage:

- Upon visiting the homepage, users are greeted with a clean layout showcasing the latest band listings.
- A prominent heading, "Band Listings", is accompanied by smaller text reading "...find your next band project, or list your own...", offering guidance to new visitors on the platform's purpose.
- If a band listing lacks a custom photo, a default placeholder image is displayed, ensuring consistency in the presentation of listings.

#### Band Listing Creation:

- Users can easily create new band listings through a form powered by crispy forms. The form is straightforward, requiring only essential details such as the band name, description, and a photo (optional).
- To streamline the process, each band listing automatically has its status set to 'Published' upon creation, without the need for manual intervention.

#### Band Listing Detail Page:

- Clicking on a band listing from the homepage leads to a detailed view. Users can view more information about the band, including a photo, and full description. The design ensures that even if no photo is provided, a default image is shown for a seamless viewing experience.

#### Inbox and Messaging:

- The application includes an inbox for handling communication between users. If a user has unread messages, a red alert icon is visible in the navbar, ensuring that important messages aren't missed.
- The inbox system is integrated into the homepage for quick access.

#### User Feedback:

- The UI incorporates Bootstrap to ensure responsive design, making the platform accessible across devices.
- Notifications, modals (such as the deletion confirmation in the band listing detail), and alerts are designed to be minimal yet effective, reducing any friction in user interaction.

#### Future Enhancements:

- The project aims to continuously improve user experience by considering feedback and adding features such as:

  * Advanced search functionality for filtering band listings by genre, location, or other criteria.
  * Enhanced profile pages for band creators to showcase their previous projects.
  * Notification systems to alert users of new listings matching their preferences.