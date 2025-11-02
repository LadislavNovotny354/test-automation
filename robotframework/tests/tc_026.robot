*** Settings ***
Resource    ../resources/common.resource

*** Test Cases ***
RF-026 Verify navigation to novinky
    Open Browser    ${DEMO_URL}    ${BROWSER}
    Click Link    Novinky
    Location Should Contain    novinky
    Close Browser
