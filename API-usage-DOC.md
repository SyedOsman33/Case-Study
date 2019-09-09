Refer to following for Guidelines to use APIs.

1. http://locahost:8080/users/get_user_by_id/[user_id]/
    Description: Returns an Object containing details about the requested user
    Params: index number as request param, i.e. http://localhost:8080/users/get_user_by_id/18/
    Method: GET 
    
2. http://localhost:8080/users/get_users_by_name?name=[user_name]
    Description: Returns a list of users where either firstname or lastname matches
    Params: [name] query param with desired string.
    Method: GET
    
3. http://localhost:8080/users/add_user/
    Description: Save a users record.
    Params: *[emails] comma seperated email of the user
            *[phone_numbers] comma seperated phone_numbers of the user
            [first_name] first_name of user
            [last_name] last_name of user
            
    *enter without comma's if only 1 record
    Method: POST
    
4. http://localhost:8080/users/edit_contact_info/
    Description: Edits a specific Contact detail record for the given user
    Params: [id] Users ID
            [email] new email to be saved
            [email_id] existing email's index ID
            [phone_number] new phone number to be saved
            [phone_id] existing phone no's index ID
    Method: POST
    
5. http://localhost:8080/users/edit_user/
    Description: Edit given user's firstname or lastname
    Params: [id] user's index ID
            [first_name] new first name
            [last_name] new last name
    Method: PATCH
    
6. http://localhost:8080/users/add_contact_info/
    Description: Add aditional contact information for given user.
    Params: [id] user's index ID
            [phone_number] Phone number
            [email] Email
    Method: POST
    
7. http://localhost:8080/users/delete_user/[user_id]/
    Description: delete the given user.
    Params: index number as request param, i.e. http://localhost:8080/users/get_user_by_id/18/
    Method: DELETE