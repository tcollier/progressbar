# Progress Cocktail Bar 

## Setup

```shell
source venv/bin/activate  # optional
pip install -r requirements.txt
cd frontend
npm install 
```

## To run locally

```shell
flask run
```

Then visit [your local host](http://127.0.0.1:5000/)

## Updating React app

If you make changes to the React app, run the following

```shell
cd frontend
npm run build
```

**IMPORTANT: Be sure to build the React app before committing changes and deploying to production**

## To deploy to production

When the `main` branch on [this GitHub repo](https://github.com/tcollier/progressbar) is updated,
changes will be automatically deployed to [the Heroku app (btcpp-progress-ba)](https://dashboard.heroku.com/apps/btcpp-progress-bar)

[Production Site](https://btcpp-progress-bar.herokuapp.com/)
