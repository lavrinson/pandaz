const express = require('express');
const axios = require('axios');
const bodyParser = require('body-parser');
require('dotenv').config();

const app = express();
const port = process.env.PORT || 5000;

app.use(bodyParser.json());

app.post('/auth/telegram', async (req, res) => {
  const { token } = req.body;
  try {
    const response = await axios.post('https://api.telegram.org/bot7159758028:AAGDG1OuKEdt5da18SHNEBKufCNSjuyee7Q/getMe');
    if (response.data.ok) {
      res.json(response.data.result);
    } else {
      res.status(400).json({ error: 'Invalid token' });
    }
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
