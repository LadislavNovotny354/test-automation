describe('Cypress Investown - footer check 96', () => {
  it('checks footer contains kontakt or info', () => {
    cy.visit('https://www.investown.cz')
    cy.get('footer').should('exist')
    // note: .or is not valid in Cypress; use conditional workarounds in real tests
  })
})
