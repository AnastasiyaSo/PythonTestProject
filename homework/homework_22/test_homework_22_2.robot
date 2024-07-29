*** Settings ***
Library  ../homework_11/homework_11_2.py
Library    BuiltIn

*** Variables ***
${DEPOSIT_AMOUNT}     ${1000}
${DEPOSIT_TIME}    ${10}
${PERCENT}     ${10}

${DEPOSIT_AMOUNT2}     invalid
${DEPOSIT_TIME2}    ${10}
${PERCENT2}     ${10}

*** Test Cases ***

Test calculate deposit amount successfully
    ${bank}=    Create Bank
    ${deposit}=    Create Deposit    ${DEPOSIT_AMOUNT}    ${DEPOSIT_TIME}    ${PERCENT}
    ${result}=  Calculate deposit amount    ${bank}    ${deposit}
    Should Be Equal As Numbers    ${result}    1086.53
    Log To Console    Deposit amount is correct

Test invalid deposit amount
    ${result}=    Run Keyword And Ignore Error    Create Deposit    ${DEPOSIT_AMOUNT2}    ${DEPOSIT_TIME2}    ${PERCENT2}
    Should Contain    ${result[1]}    Invalid deposit amount
    Log To Console    Invalid deposit amount test passed

*** Keywords ***

Create Bank
    [Arguments]
    ${bank}=    Evaluate    homework_11_2.Bank()
    RETURN    ${bank}
    
Create Deposit
    [Arguments]    ${deposit_amount}    ${deposit_time}    ${percent}
    ${deposit}=    Evaluate    homework_11_2.Deposit("${deposit_amount}", ${deposit_time}, ${percent})
    RETURN    ${deposit}

Calculate deposit amount
    [Arguments]    ${bank}    ${deposit}
    ${result}=    Call Method    ${bank}    method_deposit    ${deposit}
    RETURN    ${result}
