describe('Cypress Investown - cookie 20', () => {
  it('accept cookie if present', () => {
    cy.visit('https://www.investown.cz')
    cy.get('button').contains('Přijmout').click({force: true})
  })
})
