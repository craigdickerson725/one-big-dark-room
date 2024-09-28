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

### Colour Scheme

The One Big Dark Room project utilizes a carefully chosen color scheme to enhance readability, user engagement, and ease of navigation. The color palette is simple yet effective, creating a clean and modern aesthetic.

#### Primary Background Color:

- The overall background is a dark shade that provides a sleek, modern look, evoking a professional and focused atmosphere. This dark theme helps other elements stand out while reducing eye strain during prolonged use.

#### Text Colors:

- The default text color is white, ensuring high contrast against the dark background for easy readability.

#### Hover Effects: 

- Interactive elements, such as buttons and message alerts, utilize hover effects with color shifts to signal interactivity.

#### Buttons and Alerts:

- Important actions like creating a listing or confirming actions (such as deletion) are styled with buttons that use clear, distinguishable colors, typically leaning towards neutral or dark themes to maintain consistency with the overall design. The modal confirmation buttons (like the 'Yes' button) are styled without extra borders to create a clean appearance.

#### Visual Alerts:

- New messages in the inbox are marked with a red alert icon, ensuring that users can quickly identify pending actions or notifications.

This color scheme balances functionality with aesthetics, ensuring a visually pleasing experience without overwhelming the user with bright or excessive color variations.

### Typography

One Big Dark Room uses a clean and modern Palanquin Dark font throughout the application. The typography is designed to be minimal and readable, complementing the dark-themed background. Headings and important elements are slightly larger to establish hierarchy, while body text remains simple and easy to scan, ensuring a user-friendly reading experience across all devices.

- [Palanquin Dark](https://fonts.google.com/specimen/Palanquin Dark) was used for the primary headers and titles.

## User Stories

### Site Users

- As a Site User I can see a paginated view of all published band listings so that I can quickly search for ones that appeal to me.
- As a Site User I can open an individual band listing so that I can read the full text of the listing.
- As a Site User I can create a user account so that I can use the full features of the site.
- As a Site User I can create a band listing so that I can connect with the community of other musicians on the site.
- As a Site User I can edit or delete my band listing so that my listing is always accurate/up-to-date, or removed from the site.
- As a Site User I can message an artist via their band listing so that I can propose a collaboration.
- As a Site User I can receive messages from other users so that I can communicate with them about possible collaborations.
- As a Site User I can reply to messages so that I can respond to and interact with other users.

### Site Admin

- As a Site Administrator I can create, read, update, and delete band listings so that I can manage the content of my site.
- As a Site Administrator I can create draft band listings so that I can complete the band listing at a later time.

## Wireframes

To follow best practice, wireframes were developed for mobile, and desktop sizes.
I've used [Balsamiq](https://balsamiq.com/wireframes) to design my site wireframes.

<details>
<summary> Click here to see the Mobile Wireframes </summary>

Home
  - ![screenshot](documentation/wireframes/wireframe01.png)

Login
  - ![screenshot](documentation/wireframes/wireframe04.png)

Logout
  - ![screenshot](documentation/wireframes/wireframe05.png)

Sign Up
  - ![screenshot](documentation/wireframes/wireframe06.png)

Create Listing
  - ![screenshot](documentation/wireframes/wireframe02.png)

Inbox
  - ![screenshot](documentation/wireframes/wireframe03.png)

</details>