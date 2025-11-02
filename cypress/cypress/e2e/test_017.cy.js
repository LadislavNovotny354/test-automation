describe('Cypress Investown - smoke 17', () => {
  it('basic smoke', () => {
    cy.visit('https://www.investown.cz')
    cy.title().should('include', 'Investown')
  })
})
