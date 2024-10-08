# Testing

In this section, I aim to demonstrate that comprehensive testing has been conducted throughout the development of One Big Dark Room. The goal is to ensure that the website operates as expected, providing a seamless experience for all users while achieving its intended functionality.

To this end, each feature has been tested to confirm that it works as intended. This includes feature-by-feature testing, user experience testing, compatibility checks, and performance assessments. I have carefully evaluated the project to ensure it delivers an easy and intuitive way for users to achieve their goals.

- Feature-by-Feature Testing: Each feature of the site has been individually tested to confirm that it performs as expected.

    - Navigation: All navigation links have been tested to ensure they direct users to the correct destinations without errors. Smooth transitions between pages are confirmed.

    - Responsive Design: The website was tested across a range of devices and screen sizes to verify compatibility and ensure that all elements adapt appropriately, delivering an optimal experience on desktops, tablets, and mobile devices.

    - Band Listing Display: The band listings were checked to ensure that all content is properly displayed, with accurate descriptions, images, and functional links to additional details.

    - Contact and Messaging System: The messaging functionality was tested by sending messages between users and confirming that notifications are displayed, messages are correctly delivered, and the inbox/outbox works as intended.

- User Experience Testing
    - Usability Testing: Real users were invited to interact with the site, and their feedback was documented. Issues encountered were promptly addressed, and improvements were implemented to ensure a smooth, user-friendly experience.

    - Accessibility Testing: Testing was conducted to ensure the site complies with accessibility standards, including screen reader compatibility, proper use of alt text for images, and effective keyboard navigation.

- Compatibility Testing
    - Browser Compatibility: The website has been tested across popular web browsers such as Chrome, Firefox, and Edge to ensure consistent performance.

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
| band_listing | 404.html | ![screenshot](documentation/validation/screenshot404.png) | |
| band_listing | login.html | ![screenshot](documentation/validation/screenshot-login.png) | |
| band_listing | logout.html | ![screenshot](documentation/validation/screenshot-logout.png) | |
| band_listing | signup.html | ![screenshot](documentation/validation/screenshot-signup.png) | |

Please note that the signup.html page has a known bug that is caused by allauth.  It will also be noted below in a dedicated bug section.

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
| band_listing | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/raw.githubusercontent.com/craigdickerson725/one-big-dark-room/main/band_listing/models.py) | ![screenshot](documentation/validation/screenshot12.png) | |
| band_listing | test_forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/one-big-dark-room/main/band_listing/tests/test-forms.py) | ![screenshot](documentation/validation/test-forms.png) | |
| band_listing | test_views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/craigdickerson725/one-big-dark-room/main/band_listing/tests/test-views.py) | ![screenshot](documentation/validation/test-views.png) | |
| band_listing | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/raw.githubusercontent.com/craigdickerson725/one-big-dark-room/main/band_listing/urls.py) | ![screenshot](documentation/validation/screenshot13.png) | |
| band_listing | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/raw.githubusercontent.com/craigdickerson725/one-big-dark-room/main/band_listing/views.py) | ![screenshot](documentation/validation/screenshot14.png) | |
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

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/lighthouse/lighthouse-home-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-home-desktop.png) | Some minor warnings |
| Login | ![screenshot](documentation/lighthouse/lighthouse-login-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-login-desktop.png) | Some minor warnings |
| Signup | ![screenshot](documentation/lighthouse/lighthouse-signup-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-signup-desktop.png) | Some minor warnings |
| Create | ![screenshot](documentation/lighthouse/lighthouse-create-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-create-desktop.png) | Some minor warnings |
| Inbox | ![screenshot](documentation/lighthouse/lighthouse-inbox-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-inbox-desktop.png) | Some minor warnings |
| Logout | ![screenshot](documentation/lighthouse/lighthouse-logout-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-logout-desktop.png)

## Defensive Programming

In the One Big Dark Room project, defensive programming practices are implemented to ensure the application remains robust and handles errors gracefully. Several strategies have been used across views, forms, and models to prevent potential issues such as invalid inputs, unauthorized access, or system failures.

- Form Validation
	- BandListingForm and MessageForm both include validation logic to ensure that required fields are populated and data is in 	the expected format.
		- For example, the band_name field in the BandListingForm is required, and if it is missing, the form will return an 		error rather than allowing invalid data into the system.
		- Similarly, the message_body field in the MessageForm ensures that no empty messages can be submitted by users.
	- Unit tests have been written to cover various scenarios:
		- Forms with missing or invalid data are correctly identified as invalid.
		- Valid data (including optional fields like snippet or an image upload) is accepted.
- View-Level Protections
	- Views are protected to ensure that only authenticated users can access certain pages like creating, editing, or deleting  	listings. Unauthorized users are redirected appropriately.
	- For example, tests ensure that if a user attempts to create or edit a band listing without being logged in, they are 	redirected to the login page.
	- Additionally, views that perform CRUD operations on the BandListing model (e.g., edit_listing and delete_listing) check  	whether the logged-in user has permission to modify the resource, ensuring that only the listing's creator can make changes.
- Database Integrity
	- In the BandListing and Message models, Django’s built-in validations, such as required fields and foreign key 	relationships, prevent invalid data from being saved to the database.
	- For example, BandListing ensures that each band has a unique slug, and the Message model prevents the creation of messages 	without a sender, recipient, or associated listing.
	- Unit tests verify the proper creation, updating, and deletion of model instances, ensuring data integrity.
- Graceful Handling of Missing Data
	- In views and templates, missing data is handled gracefully:
		- For instance, when a band listing does not include a photo, the template falls back to a default image rather than 		breaking.
		- The pagination controls ensure that users cannot navigate to non-existent pages (e.g., previous or next links are 		disabled when on the first or last page, respectively).
		- Tests verify that the application properly handles empty data states, such as no band listings being available.
- Error Feedback and User-Friendly Responses
	- Error messages are displayed to users when something goes wrong, such as submitting invalid form data. These errors are 	clearly indicated in forms, helping users correct their inputs.
	- Tests are in place to confirm that the appropriate error messages are shown when forms are submitted with invalid data.
    
By combining these defensive strategies with thorough testing, the One Big Dark Room project is designed to be resilient to unexpected inputs and conditions, ensuring a reliable and user-friendly experience.

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| Home | | | | | |
| | Band listings should display correctly, including band photo, name, and snippet | Navigated to the home page | Band listings appeared with the correct details and placeholder image where no photo is uploaded | Test concluded and passed | ![screenshot](documentation/features/feature01x.png) |
| | Pagination should allow navigating through pages of band listings | Clicked 'Next' and 'Previous' pagination links | Pagination worked as expected, displaying the correct listings for each page | Test concluded and passed | ![screenshot](documentation/features/feature02x.png) |
| Login | | | | | |
| | Users should be able to log in with valid credentials | Entered valid username and password and submitted form | Login succeeded, and the user was redirected to the home page | Test concluded and passed | ![screenshot](documentation/features/feature03x.png) |
| | Error message should display for invalid credentials | Entered invalid username/password and submitted form | An error message appeared as expected | Test concluded and passed | ![screenshot](documentation/features/feature04x.png) |
| Sign Up | | | | | |
| | Users should be able to sign up with valid details | Entered valid signup details | Signup succeeded, and the user was redirected to the home page | Test concluded and passed | ![screenshot](documentation/features/feature05x.png) |
| | Error message should display for invalid or missing details | Left required fields empty and submitted form | The form displayed validation errors as expected | Test concluded and passed | ![screenshot](documentation/features/feature06x.png) |
| Create Listing | | | | | |
| | Users should be able to create a band listing with valid details | Submitted the form with valid data | The listing was created successfully, and I was redirected to the band detail page | Test concluded and passed | ![screenshot](documentation/features/feature07x.png) |
| | Error message should display for missing required fields | Submitted form without 'band_name' | An error message appeared as expected | Test concluded and passed | ![screenshot](documentation/features/feature08x.png) |
| Edit Listing | | | | | |
| | Users should be able to edit their band listing details | Tested the feature by doing Y | The listing was updated successfully | Test concluded and passed | ![screenshot](documentation/features/feature09x.png) |
| | Error message should display for invalid input | Submitted form with invalid data | Error message displayed for invalid fields | Test concluded and passed | ![screenshot](documentation/features/feature10x.png) |
| Send Message | | | | | |
| | Users should be able to send messages from a band listing page | Sent a valid message from a band listing | Message was sent, and I was redirected to the messages page | Test concluded and passed | ![screenshot](documentation/features/feature11x.png) |
| | Error message should display for empty message body | Submitted form with an empty message body | Error message displayed as expected | Test concluded and passed | ![screenshot](documentation/features/feature12x.png) |
| Inbox | | | | | |
| | Inbox should display received messages correctly | Navigated to the inbox | Messages were displayed with correct details | Test concluded and passed | ![screenshot](documentation/features/feature13x.png) |
| Bandlisting Details | | | | | |
| | Bandlisting details page should show all relevant details of the band | Viewed a band listing’s details page | All information (band name, photo, description, and snippet) appeared correctly | Test concluded and passed | ![screenshot](documentation/features/feature15x.png) |
| | Default image should appear if no band photo is uploaded | Viewed a band listing with no photo | Default placeholder image displayed as expected | Test concluded and passed | ![screenshot](documentation/features/feature16x.png) |
| Message Details | | | | | |
| | User should be able to view details of a message | Clicked on a message in the inbox | The message was displayed with all details (sender, recipient, and body) | Test concluded and passed | ![screenshot](documentation/features/feature14x.png) |
| 404 Error | | | | | |
| | User should see a custom 404 error page when navigating to a non-existent page | Navigated to a non-existent URL | Custom 404 error page appeared with the correct message | Test concluded and passed | ![screenshot](documentation/features/feature19x.png) |
| | Custom 404 page should have a link to return to the home page | Checked for the 'Return to Home' link on the 404 page | Link was present and functioned as expected | Test concluded and passed | ![screenshot](documentation/features/feature20x.png) |
| Logout | | | | | |
| | User should be logged out and redirected to the login page | Clicked the 'Logout' link | Logout succeeded, and I was redirected to the login page | Test concluded and passed | ![screenshot](documentation/features/feature21x.png) |

## User Story Testing

| User Story | Screenshot |
| --- | --- |
| As a Site User I can see a paginated view of all published band listings so that I can quickly search for ones that appeal to me. | ![screenshot](documentation/features/feature01.png) |
| As a Site User I can open an individual band listing so that I can read the full text of the listing. | ![screenshot](documentation/features/feature02.png) |
| As a Site User I can create a user account so that I can use the full features of the site. | ![screenshot](documentation/features/feature05a.png) |
| As a Site User I can create a band listing so that I can connect with the community of other musicians on the site. | ![screenshot](documentation/features/feature06.png) |
| As a Site User I can edit or delete my band listing so that my listing is always accurate/up-to-date, or removed from the site. | ![screenshot](documentation/features/feature07b.png) |
| As a Site User I can message an artist via their band listing so that I can propose a collaboration. | ![screenshot](documentation/features/feature08b.png) |
| As a Site User I can receive messages from other users so that I can communicate with them about possible collaborations. | ![screenshot](documentation/features/feature09b.png) |
| As a Site User I can reply to messages so that I can respond to and interact with other users. | ![screenshot](documentation/features/feature10a.png) |
| As a Site Administrator I can create, read, update, and delete band listings so that I can manage the content of my site. | ![screenshot](documentation/features/feature03a.png) |
| As a Site Administrator I can create draft band listings so that I can complete the band listing at a later time. | ![screenshot](documentation/features/feature04.png) |
| As a Site User I can delete the messages in my inbox and outbox so that I can clear out messages that I no longer need. | ![screenshot](documentation/features/feature11a.png) |

## Automated Testing

I have conducted a series of automated tests on my application.

I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

### Form Tests

#### Overview
Form testing ensures that user inputs are validated and processed correctly. In this project, I tested the forms to verify that data is appropriately validated before submission.

The tests were written using **Django's test framework**, which provides tools for checking form behavior, field validation, and error handling.

#### Band Listing Form

- **Test Case: Valid Data Submission**
  - **Description:** Tests if the form accepts valid data for all required fields (`band_name`, `snippet`, etc.).
  - **Expected Outcome:** The form should be valid, and a new band listing should be created upon submission.
  - **Actual Outcome:** The form was valid, and the listing was successfully created.

- **Test Case: Missing Required Fields**
  - **Description:** Tests the form's validation when required fields are left blank.
  - **Expected Outcome:** The form should return errors for the missing fields.
  - **Actual Outcome:** Validation errors were correctly displayed for missing fields.

#### Message Form

- **Test Case: Valid Data Submission**
  - **Description:** Ensures that the form accepts valid data for the message body and recipient.
  - **Expected Outcome:** The form should be valid, and the message should be sent.
  - **Actual Outcome:** The form was successfully submitted, and the message was sent as expected.

- **Test Case: Empty Message Body**
  - **Description:** Tests form validation when the message body is empty.
  - **Expected Outcome:** The form should be invalid, with an error message for the missing body.
  - **Actual Outcome:** The form returned the expected validation error.

---

### View Tests

#### Overview
View testing ensures that the application's pages render correctly and that the expected data is returned to the user. I used **Django's test client** to simulate GET and POST requests, verifying that the correct views were called, and the right templates were rendered.

#### Band Listing Views

- **Test Case: Listing Page Renders Successfully**
  - **Description:** Checks if the band listing page loads correctly.
  - **Expected Outcome:** The page should return a 200 status code and render the correct template (`band_listing.html`).
  - **Actual Outcome:** The page loaded successfully with a 200 status code and rendered the correct template.

- **Test Case: Band Detail Page**
  - **Description:** Tests whether the detail page for a specific band listing renders properly when accessed by its slug.
  - **Expected Outcome:** The page should return a 200 status code and render the `band_detail.html` template.
  - **Actual Outcome:** The page was rendered correctly, and the expected content was displayed.

#### Message Views

- **Test Case: Inbox Renders Successfully**
  - **Description:** Ensures that the inbox page for the logged-in user is accessible and displays messages.
  - **Expected Outcome:** The inbox should load with a 200 status code and list any available messages.
  - **Actual Outcome:** The inbox page rendered successfully, displaying the correct messages for the logged-in user.

- **Test Case: Message Deletion**
  - **Description:** Tests whether a message can be successfully deleted.
  - **Expected Outcome:** The message should be flagged as deleted and no longer appear in the inbox or outbox.
  - **Actual Outcome:** The message was marked as deleted and was no longer visible in either the inbox or outbox.

---

#### How to Run the Tests

To run the form and view tests using Django's test framework, use the following command:

```bash
python3 manage.py test
```
#### My Results

The screenshot below shows the passing results of the automated tests for testing the views and testing the forms:

![screenshot](documentation/automated_testing.png)

### Test Coverage

#### Overview
Test coverage was measured using **coverage.py** to ensure that key parts of the application are tested. This helps identify areas of the code that still need testing and verifies that the majority of the project is being covered by the test suite.

#### Coverage Results
After running the test suite, the overall coverage percentage was:

**87%**

Here is a breakdown of the coverage for different parts of the project:

| File                                | Statements | Missed | Coverage |
|-------------------------------------|------------|--------|----------|
| `band_listing/admin.py`             | 20         | 1      | 95%      |
| `band_listing/apps.py`              | 4          | 0      | 100%     |
| `band_listing/context_processors.py`| 6          | 0      | 100%     |
| `band_listing/forms.py`             | 26         | 0      | 100%     |
| `band_listing/models.py`            | 43         | 6      | 86%      |
| `band_listing/tests/test_forms.py`  | 48         | 1      | 98%      |
| `band_listing/tests/test_views.py`  | 52         | 0      | 100%     |
| `band_listing/urls.py`              | 4          | 0      | 100%     |
| `band_listing/views.py`             | 141        | 42     | 70%      |
| `manage.py`                         | 11         | 2      | 82%      |
| `onebigdarkroom/settings.py`        | 37         | 0      | 100%     |
| `onebigdarkroom/urls.py`            | 5          | 0      | 100%     |
| `onebigdarkroom/views.py`           | 3          | 1      | 67%      |
| **TOTAL**                           | 400        | 53     | **87%**  |

To generate the coverage report, the following command was used:

```bash
coverage run --omit=*/site-packages/*,*/migrations/*,*/__init__.py,env.py manage.py test
```
The HTML coverage report can be generated and viewed with:

```bash
coverage html
```
This opens a detailed report of which lines of code were executed during testing.

![screenshot](documentation/coverage_report.png)

## Bugs

The only known bug with the application is a well-known error caused by the allauth authentication system in Django, which appears on the Sign Up page.  This was caught in the validation process, and confirmed to me by my mentor, Tim Nelson.

![screenshot](documentation/validation/screenshot-signup.png)

## Unfixed Bugs

The only bug that I am aware of is the above mentioned 'allauth' error on the Sign Up page.  While this bug remains unfixed, it does not disrupt the functionality of the signup process, so it will remain unnoticed by users.


> [!NOTE]  
> There are no remaining bugs that I am aware of.