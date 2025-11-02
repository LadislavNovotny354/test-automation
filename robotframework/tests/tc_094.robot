*** Settings ***
Resource    ../resources/common.resource

*** Test Cases ***
RF-094 Smoke title contains Investown
    Open Browser    ${DEMO_URL}    ${BROWSER}
    Title Should Contain    Investown
    Close Browser
