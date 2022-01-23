import * as React from 'react';
import { render } from 'react-dom';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import Link from '@mui/material/Link';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { createTheme, ThemeProvider } from '@mui/material/styles';


function Copyright(props) {
  return (
    <Typography variant="body2" color="text.secondary" align="center" {...props}>
      {'Copyright © '}
      <Link color="inherit" href="https://mui.com/">
        Your Website
      </Link>{' '}
      {new Date().getFullYear()}
      {'.'}
    </Typography>
  );
}

let MessageBox = (props) => {
  var object = props.name;
  //object.split('},')
  console.log(object)
  //object = JSON.parse(object)
  return (
    <Box
      sx = {{
        mt: 1
      }}
    >
      <Grid container>
        <Grid item>
          <Typography variant="body2" color="text.secondary" align="center">
            { object /*object.map(item => {
              if(item.from_user === "oscar")
                return (
                    item['body']
                )
            })*/}
          </Typography>
        </Grid>
      </Grid>
    </Box>
  );
}

const theme = createTheme();

export default class MessageList extends React.Component {
  constructor() {
    super();
    this.state = { showMessage: false,
                   responseText: "" }
  }

  _showMessage = (bool) => {
    this.setState({
      showMessage: bool
    });
  }
  
  handleSubmit = (event) => {
    event.preventDefault();
    let xhr = new XMLHttpRequest();
    xhr.addEventListener('load', () => {
      this.setState({
        responseText: xhr.responseText
      });
    })
    xhr.open('GET', 'http://127.0.0.1:8000/messages/');
    xhr.setRequestHeader('Content-type', 'application/json');
    xhr.setRequestHeader("Authorization", "Token " + localStorage.getItem('token'));
    xhr.send();
  };

  render() {
    return (
      <ThemeProvider theme={theme}>
        <Container component="main" maxWidth="xs">
          <CssBaseline />
          <Box component="form" onSubmit={this.handleSubmit} noValidate sx={{ mt: 1 }}>
            <Button
              type="submit"
              onClick={this._showMessage}
              fullWidth
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
            >
              Get Messages
            </Button>
          </Box>
          <Box
            id = 'messages'
            sx={{
              marginTop: 8,
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
            }}
          >
            { this.state.showMessage && (<MessageBox name={this.state.responseText}/>) }
          </Box>
          <Copyright sx={{ mt: 8, mb: 4 }} />
        </Container>
      </ThemeProvider>
    )
  }
}