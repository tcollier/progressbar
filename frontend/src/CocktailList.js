import React from 'react';

function App({ cocktails }) {
  return (
      <ul className="Cocktail">
        {cocktails.map(function(cocktail) {
          return (<li>{cocktail.name}</li>)
        })}
      </ul>
  );
}

export default App;
