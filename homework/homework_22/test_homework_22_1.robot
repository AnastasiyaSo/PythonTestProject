*** Settings ***
Library  ../homework_11/homework_11_1.py
Library    BuiltIn

*** Variables ***
${CLIENT_ID_1}     1
${FIRST_NAME_1}    Peter
${LAST_NAME_1}     Ivanov
${NAME_BOOK_1}      Harry Potter 3
${AUTHOR_1}    J. K. Rowling
${ISBN_1}  5

${CLIENT_ID_2}     2
${FIRST_NAME_2}    Slava
${LAST_NAME_2}     Petrov
${NAME_BOOK_2}      Harry Potter 4
${AUTHOR_2}    J. K. Rowling
${ISBN_2}  6

${CLIENT_ID_3}     3
${FIRST_NAME_3}    Olya
${LAST_NAME_3}     Petrova
${NAME_BOOK_3}      Harry Potter 5
${AUTHOR_3}    J. K. Rowling
${ISBN_3}  7

${CLIENT_ID_4}     4
${FIRST_NAME_4}    Alex
${LAST_NAME_4}     Ford

${CLIENT_ID_5}     5
${FIRST_NAME_5}    Kate
${LAST_NAME_5}     Ford
${NAME_BOOK_5}      Harry Potter 6
${AUTHOR_5}    J. K. Rowling
${ISBN_5}  8

${CLIENT_ID_6}     6
${FIRST_NAME_6}    Alex
${LAST_NAME_6}     Antonov
${NAME_BOOK_6}      Harry Potter 7
${AUTHOR_6}    J. K. Rowling
${ISBN_6}  9

*** Test Cases ***

Test verify client can take book
    ${client}=    Create Client    ${CLIENT_ID_1}   ${FIRST_NAME_1}    ${LAST_NAME_1}
    ${book}=    Create Book    ${NAME_BOOK_1}    ${AUTHOR_1}    ${ISBN_1}
    ${result}=  Take Book    ${client}    ${book}
    Should Be Equal    ${book.taken_by}    ${client.client_id}
    Log To Console    Client can take book

Test verify client can reserve book
    ${client}=    Create Client    ${CLIENT_ID_2}   ${FIRST_NAME_2}    ${LAST_NAME_2}
    ${book}=    Create Book    ${NAME_BOOK_2}    ${AUTHOR_2}    ${ISBN_2}
    ${result}=  Reserve Book   ${client}    ${book}
    Should Be Equal    ${book.reserved_by}    ${client.client_id}
    Log To Console    Client can reserve book
    
Test verify client can not reserve book
    ${client}=    Create Client    ${CLIENT_ID_3}   ${FIRST_NAME_3}    ${LAST_NAME_3}
    ${book}=    Create Book    ${NAME_BOOK_3}    ${AUTHOR_3}    ${ISBN_3}
    ${result}=  Reserve Book   ${client}    ${book}
    ${client2}=    Create Client    ${CLIENT_ID_4}   ${FIRST_NAME_4}    ${LAST_NAME_4}
    ${result2}=  Reserve Book   ${client2}    ${book}
    Should Not Be True    ${result2}
    Log To Console    ${NAME_BOOK_3} is reserved by another client

Test verify client can return book
    ${client}=    Create Client    ${CLIENT_ID_5}   ${FIRST_NAME_5}    ${LAST_NAME_5}
    ${book}=    Create Book    ${NAME_BOOK_5}    ${AUTHOR_5}    ${ISBN_5}
    ${result}=  Take Book   ${client}    ${book}
    ${result2}=  Return Book   ${client}    ${book}
    Should Be True    ${result2}
    Log To Console    ${NAME_BOOK_5} is returned successfully

Test verify client can not return book
    ${client}=    Create Client    ${CLIENT_ID_6}   ${FIRST_NAME_6}    ${LAST_NAME_6}
    ${book}=    Create Book    ${NAME_BOOK_6}    ${AUTHOR_6}    ${ISBN_6}
    ${result}=  Return Book   ${client}    ${book}
    Should Not Be True    ${result}
    Log To Console    ${NAME_BOOK_6} is not taken


*** Keywords ***

Create Client
    [Arguments]    ${client_id}    ${first_name}    ${last_name}
    ${client}=    Evaluate    homework_11_1.Client("${client_id}", "${first_name}", "${last_name}")
    RETURN    ${client}

Create Book
    [Arguments]    ${name_book}    ${author}    ${isbn}
    ${book}=    Evaluate    homework_11_1.Book("${name_book}", "${author}", "${isbn}")
    RETURN    ${book}
    
Take Book
    [Arguments]    ${client}    ${book}
    ${result}=    Call Method    ${client}    take_book    ${book}
    RETURN    ${result}

Reserve Book
    [Arguments]    ${client}    ${book}
    ${result}=    Call Method    ${client}    reserve_book    ${book}
    RETURN    ${result}

Return Book
    [Arguments]    ${client}    ${book}
    ${result}=    Call Method    ${client}    return_book    ${book}
    RETURN    ${result}
