# User Profiler

A backend application to create and update User Profiles

## Installation

- The App has a backend (on Local server).
- Clone the repo using `git clone`(use https in order to avoid any ssh key related issues)

  ### Backend

  - Backend in Python using Django Rest Framework and has sqlite3 as a database.
  - After cloning the repo, navigate to `backend` folder and execute the following commands

    ```python
    python manage.py makemigrations
    python manage.py migrate
    ```

  - This will migrate the used models on the DB.
  - Now spin up the local server by executing the below command
    ```python
    python manage.py runserver
    ```
  - Server will be available on `http://127.0.0.1:8000`
  - `BaseUrl` is `http://127.0.0.1:8000/`

## Routes

- The project has two apps:

  - UserAuth
  - UserProfile

  ### UserAuth

  - This app handles the user authorization and authentication
  - It has 3 routes
    - User signUp ➡`BaseUrl/userauth/signUp`
    - Get access token ➡ `BaseUrl/userauth/token`
    - Refresh access token ➡ `BaseUrl/userauth/token/refresh`

  ### UserProfile

  - This app handles the user profile creation and updation.
  - It has 2 routes
    - New Profile creation ➡ `BaseUrl/profile/newProfile`
    - Update an existing profile ➡ `BaseUrl/profile/updateProfile`

## Request Params and Body

- As we have 2 diff apps, they will accept different request params and body contents from the Postman.

  ### UserAuth

  - The 3 routes will have the below mentioned request format.
    #### signUp
          - POST request
          - username and password in form-encoded body
    #### token
          - POST request
          - username and password in form-encoded body
    #### refresh token
          - POST request
          - refresh token in the form-encoded body

  ### UserProfile

  - The 2 routes will have the below mentioned request format

    #### newProfile

          - POST request

          - profile_id(int) --> must be unique for every profile
          - name(string) --> Profile name
          - email(string) --> Email id
          - bio(string) --> Bio for the profile
          - pic(string) --> Picture is kept as string for now as I was unable to find a way post jpg/png image via an API call
          -  All the above fields must be passed in form-encoded body

          - Authorization Bearer<access_token> must be set in the Headers

    #### updateProfile

          - PATCH request

          - Provide the Profile fields which you want to update in form-encoded body

          - profile_id --> should be passed in Query params

          - Authorization Bearer<access_token> must be set in the Headers

    - `Note that Only the Authorised users will be allowed to create or update their profiles and current logged in user will be able to update it's own profile`

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
