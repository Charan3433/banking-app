import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { Button, Card, CardContent, Typography, Stack } from '@mui/material';
import axios from 'axios';

const TransactionsPage = () => {
  const [transactions, setTransactions] = useState([]);

  useEffect(() => {
    const fetchTransactions = async () => {
      const token = localStorage.getItem('token');
      const res = await axios.get('/api/transactions', { headers: { Authorization: `Bearer ${token}` } });
      setTransactions(res.data.transactions);
    };
    fetchTransactions();
  }, []);

  return (
    <div>
      <Typography variant="h4" gutterBottom>Transactions</Typography>
      <Button component={Link} to="/dashboard" variant="outlined" sx={{ mb: 2 }}>Back</Button>
      <Stack spacing={2}>
        {transactions.map((tx) => (
          <Card key={tx.id}>
            <CardContent>
              <Typography variant="h6">{tx.transaction_type}</Typography>
              <Typography color="text.secondary">{tx.description}</Typography>
              <Typography>Amount: ${Number(tx.amount).toFixed(2)}</Typography>
            </CardContent>
          </Card>
        ))}
      </Stack>
    </div>
  );
};

export default TransactionsPage;
