import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { Button, Card, CardContent, Grid, Typography } from '@mui/material';
import axios from 'axios';

const AccountsPage = () => {
  const [accounts, setAccounts] = useState([]);

  useEffect(() => {
    const fetchAccounts = async () => {
      const token = localStorage.getItem('token');
      const res = await axios.get('/api/accounts', { headers: { Authorization: `Bearer ${token}` } });
      setAccounts(res.data.accounts);
    };
    fetchAccounts();
  }, []);

  return (
    <div>
      <Typography variant="h4" gutterBottom>Accounts</Typography>
      <Button component={Link} to="/dashboard" variant="outlined" sx={{ mb: 2 }}>Back</Button>
      <Grid container spacing={2}>
        {accounts.map((account) => (
          <Grid item xs={12} md={6} key={account.id}>
            <Card>
              <CardContent>
                <Typography variant="h6">{account.account_type}</Typography>
                <Typography color="text.secondary">Account Number: {account.account_number}</Typography>
                <Typography>Balance: ${Number(account.balance).toFixed(2)}</Typography>
              </CardContent>
            </Card>
          </Grid>
        ))}
      </Grid>
    </div>
  );
};

export default AccountsPage;
