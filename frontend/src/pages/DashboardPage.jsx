import { useEffect, useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { AppBar, Box, Button, Card, CardContent, Grid, Stack, Toolbar, Typography } from '@mui/material';
import axios from 'axios';

const DashboardPage = () => {
  const navigate = useNavigate();
  const [summary, setSummary] = useState({ user: {}, accounts: [], transactions: [] });

  useEffect(() => {
    const fetchData = async () => {
      const token = localStorage.getItem('token');
      const headers = { Authorization: `Bearer ${token}` };
      const [profile, accounts, transactions] = await Promise.all([
        axios.get('/api/users/profile', { headers }),
        axios.get('/api/accounts', { headers }),
        axios.get('/api/transactions', { headers }),
      ]);
      setSummary({ user: profile.data.user, accounts: accounts.data.accounts, transactions: transactions.data.transactions });
    };
    fetchData();
  }, []);

  const logout = () => {
    localStorage.removeItem('token');
    navigate('/login');
  };

  return (
    <Box>
      <AppBar position="static" sx={{ mb: 3 }}>
        <Toolbar>
          <Typography variant="h6" sx={{ flexGrow: 1 }}>Banking Dashboard</Typography>
          <Button color="inherit" component={Link} to="/accounts">Accounts</Button>
          <Button color="inherit" component={Link} to="/transactions">Transactions</Button>
          <Button color="inherit" component={Link} to="/profile">Profile</Button>
          <Button color="inherit" onClick={logout}>Logout</Button>
        </Toolbar>
      </AppBar>
      <Grid container spacing={3}>
        <Grid item xs={12} md={4}>
          <Card>
            <CardContent>
              <Typography color="text.secondary">Welcome</Typography>
              <Typography variant="h5">{summary.user.full_name}</Typography>
              <Typography mt={1}>Total Balance: ${summary.accounts.reduce((sum, account) => sum + Number(account.balance), 0).toFixed(2)}</Typography>
            </CardContent>
          </Card>
        </Grid>
        <Grid item xs={12} md={4}>
          <Card><CardContent><Typography color="text.secondary">Accounts</Typography><Typography variant="h4">{summary.accounts.length}</Typography></CardContent></Card>
        </Grid>
        <Grid item xs={12} md={4}>
          <Card><CardContent><Typography color="text.secondary">Recent Transactions</Typography><Typography variant="h4">{summary.transactions.length}</Typography></CardContent></Card>
        </Grid>
      </Grid>
      <Stack direction={{ xs: 'column', md: 'row' }} spacing={2} mt={4}>
        <Button variant="contained" component={Link} to="/deposit">Deposit</Button>
        <Button variant="contained" component={Link} to="/withdraw">Withdraw</Button>
        <Button variant="contained" component={Link} to="/transfer">Transfer</Button>
      </Stack>
    </Box>
  );
};

export default DashboardPage;
