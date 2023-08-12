const http = require('http');
const url = require('url');
const qs = require('querystring');

const tweets = ['Tweet 1', 'Tweet 2', 'Tweet 3'];

const server = http.createServer(async (req, res) => {
  const parsedUrl = url.parse(req.url);
  const path = parsedUrl.pathname;
  const query = qs.parse(parsedUrl.query);

  if (path === '/tweets') {
    if (req.method === 'GET') {
      res.setHeader('Content-Type', 'application/json');
      res.setHeader('Access-Control-Allow-Origin', '*');
      res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, DELETE');
      res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type');
      res.end(JSON.stringify(tweets));
    } else if (req.method === 'POST') {
      res.setHeader('Content-Type', 'application/json');
      res.setHeader('Access-Control-Allow-Origin', '*');
      res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, DELETE');
      res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type');
      const body = await getRequestBody(req);
      const newTweet = qs.parse(body).tweet;
      tweets.push(newTweet);
      console.log(tweets); // Log the tweets array after adding the new tweet
      res.end();
    }
  } else {
    res.end('Hello World\n');
  }

});

server.listen(3000, () => {
  console.log('Server running on port 3000');
});

function getRequestBody(req) {
  return new Promise((resolve, reject) => {
    let body = '';
    req.on('data', chunk => {
      body += chunk.toString();
    });
    req.on('end', () => {
      resolve(body);
    });
    req.on('error', err => {
      reject(err);
    });
  });
}
