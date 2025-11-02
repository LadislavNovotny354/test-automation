describe('Cypress Investown - smoke 89', () => {
  it('basic smoke', () => {
    cy.visit('https://www.investown.cz')
    cy.title().should('include', 'Investown')
  })
})
