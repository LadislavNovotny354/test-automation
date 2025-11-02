*** Settings ***
Resource    ../resources/common.resource

*** Test Cases ***
RF-093 Verify offers page elements
    Open Browser    ${DEMO_URL}/nabidka    ${BROWSER}
    Page Should Contain Element    xpath=//h1
    Page Should Contain    Investice
    Close Browser
