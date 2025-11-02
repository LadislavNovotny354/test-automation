describe('Cypress Investown - cookie 80', () => {
  it('accept cookie if present', () => {
    cy.visit('https://www.investown.cz')
    cy.get('button').contains('Přijmout').click({force: true})
  })
})
