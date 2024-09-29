In this section, I aim to demonstrate that comprehensive testing has been conducted throughout the development of One Big Dark Room. The goal is to ensure that the website operates as expected, providing a seamless experience for all users while achieving its intended functionality.

To this end, each feature has been thoroughly tested to confirm that it works as intended. This includes feature-by-feature testing, user experience testing, compatibility checks, and performance assessments. I have carefully evaluated the project to ensure it delivers an easy and intuitive way for users to achieve their goals.

- Feature-by-Feature Testing: Each feature of the site has been individually tested to confirm that it performs as expected.

    - Navigation: All navigation links have been tested to ensure they direct users to the correct destinations without errors. Smooth transitions between pages are confirmed.

    - Responsive Design: The website was tested across a range of devices and screen sizes to verify compatibility and ensure that all elements adapt appropriately, delivering an optimal experience on desktops, tablets, and mobile devices.

    - Band Listing Display: The band listings were checked to ensure that all content is properly displayed, with accurate descriptions, images, and functional links to additional details.

    - Contact and Messaging System: The messaging functionality was tested by sending messages between users and confirming that notifications are displayed, messages are correctly delivered, and the inbox/outbox works as intended.

- User Experience Testing
    - Usability Testing: Real users were invited to interact with the site, and their feedback was documented. Issues encountered were promptly addressed, and improvements were implemented to ensure a smooth, user-friendly experience.

    - Accessibility Testing: Testing was conducted to ensure the site complies with accessibility standards, including screen reader compatibility, proper use of alt text for images, and effective keyboard navigation.

- Compatibility Testing
    - Browser Compatibility: The website has been tested across popular web browsers such as Chrome, Firefox, Safari, and Edge to ensure consistent performance.

    - Device Compatibility: Functionality was tested across multiple devices, including desktops, laptops, tablets, and smartphones, to ensure that the site works properly on all platforms.

- Regression Testing
    - After implementing updates and fixes, regression testing was conducted to ensure that previously functional features remain unaffected by the changes. This process helps prevent new issues from arising due to updates.

- Documentation and Logs
    - Throughout the testing process, detailed records were maintained, including testing procedures, results, and any issues encountered. All bugs were documented, along with the steps taken to resolve them. This systematic approach helps ensure that the site continues to function correctly as it evolves.

- User Feedback Incorporation
    - User feedback played a crucial role in enhancing the overall user experience. Any issues or suggestions raised by users were evaluated, and improvements were made where necessary to ensure the site meets user expectations.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| band_listing | bandlisting_detail.html | ![screenshot](documentation/validation/screenshot01.png) | |
| band_listing | create_listing.html | ![screenshot](documentation/validation/screenshot02.png) | |
| band_listing | edit_listing.html | ![screenshot](documentation/validation/screenshot03.png) | |
| band_listing | index.html | ![screenshot](documentation/validation/screenshot04.png) | |
| band_listing | message_detail.html | ![screenshot](documentation/validation/screenshot05.png) | |
| band_listing | messages.html | ![screenshot](documentation/validation/screenshot06.png) | |
| band_listing | send_message.html | ![screenshot](documentation/validation/screenshot07.png) | |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| static | style.css | ![screenshot](documentation/validation/screenshot08.png) | |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| band_listing | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/one-big-dark-room/main/band_listing/admin.py) | ![screenshot](documentation/validation/screenshot09.png) | |
| band_listing | context_processors.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/one-big-dark-room/main/band_listing/context_processors.py) | ![screenshot](documentation/validation/screenshot10.png) | |
| band_listing | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/one-big-dark-room/main/band_listing/forms.py) | ![screenshot](documentation/validation/screenshot11.png) | |
| band_listing | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/one-big-dark-room/main/band_listing/models.py) | ![screenshot](documentation/validation/screenshot12.png) | |
| band_listing | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/one-big-dark-room/main/band_listing/urls.py) | ![screenshot](documentation/validation/screenshot13.png) | |
| band_listing | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/one-big-dark-room/main/band_listing/views.py) | ![screenshot](documentation/validation/screenshot14.png) | |
|  | manage.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/one-big-dark-room/main/manage.py) | ![screenshot](documentation/validation/screenshot15.png) | |
| onebigdarkroom | settings.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/one-big-dark-room/main/onebigdarkroom/settings.py) | ![screenshot](documentation/validation/screenshot16.png) | |
| onebigdarkroom | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/one-big-dark-room/main/onebigdarkroom/urls.py) | ![screenshot](documentation/validation/screenshot17.png) | |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home | About | Contact | etc | Notes |
| --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/browsers/browser-chrome-home.png) | ![screenshot](documentation/browsers/browser-chrome-login.png) | ![screenshot](documentation/browsers/browser-chrome-signup.png) | ![screenshot](documentation/browsers/browser-chrome-create.png) | ![screenshot](documentation/browsers/browser-chrome-inbox.png) | ![screenshot](documentation/browsers/browser-chrome-logout.png) | Works as expected |
| Firefox | ![screenshot](documentation/browsers/browser-firefox-home.png) | ![screenshot](documentation/browsers/browser-firefox-login.png) | ![screenshot](documentation/browsers/browser-firefox-signup.png) | ![screenshot](documentation/browsers/browser-firefox-create.png) | ![screenshot](documentation/browsers/browser-firefox-inbox.png) | ![screenshot](documentation/browsers/browser-firefox-logout.png) | Works as expected |
| Edge | ![screenshot](documentation/browsers/browser-edge-home.png) | ![screenshot](documentation/browsers/browser-edge-login.png) | ![screenshot](documentation/browsers/browser-edge-signup.png) | ![screenshot](documentation/browsers/browser-edge-create.png) | ![screenshot](documentation/browsers/browser-edge-inbox.png) | ![screenshot](documentation/browsers/browser-edge-logout.png) | Works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Home | About | Contact | etc | Notes |
| --- | --- | --- | --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/responsiveness/responsive-mobile-home.png) | ![screenshot](documentation/responsiveness/responsive-mobile-login.png) | ![screenshot](documentation/responsiveness/responsive-mobile-signup.png) | ![screenshot](documentation/responsiveness/responsive-mobile-create.png) | ![screenshot](documentation/responsiveness/responsive-mobile-inbox.png) | ![screenshot](documentation/responsiveness/responsive-mobile-logout.png) | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/responsiveness/responsive-tablet-home.png) | ![screenshot](documentation/responsiveness/responsive-tablet-login.png) | ![screenshot](documentation/responsiveness/responsive-tablet-signup.png) | ![screenshot](documentation/responsiveness/responsive-tablet-create.png) | ![screenshot](documentation/responsiveness/responsive-tablet-inbox.png) | ![screenshot](documentation/responsiveness/responsive-tablet-logout.png) | Works as expected |
| Desktop | ![screenshot](documentation/responsiveness/responsive-desktop-home.png) | ![screenshot](documentation/responsiveness/responsive-desktop-login.png) | ![screenshot](documentation/responsiveness/responsive-desktop-signup.png) | ![screenshot](documentation/responsiveness/responsive-desktop-create.png) | ![screenshot](documentation/responsiveness/responsive-desktop-inbox.png) | ![screenshot](documentation/responsiveness/responsive-desktop-logout.png) | Works as expected |