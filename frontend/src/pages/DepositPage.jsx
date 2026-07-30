import { useState } from 'react';
import { Link } from 'react-router-dom';
import { Button, Card, CardContent, Stack, TextField, Typography } from '@mui/material';
import axios from 'axios';

const DepositPage = () => {
  const [form, setForm] = useState({ account_id: '', amount: '' });
  const [message, setMessage] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    const token = localStorage.getItem('token');
    await axios.post('/api/transactions/deposit', { account_id: Number(form.account_id), amount: Number(form.amount) }, { headers: { Authorization: `Bearer ${token}` } });
    setMessage('Deposit completed');
  };

  return (
    <Card sx={{ maxWidth: 520, mx: 'auto', mt: 6 }}>
      <CardContent>
        <Typography variant="h4" gutterBottom>Deposit</Typography>
        <form onSubmit={handleSubmit}>
          <Stack spacing={2}>
            <TextField label="Account ID" value={form.account_id} onChange={(e) => setForm({ ...form, account_id: e.target.value })} />
            <TextField label="Amount" value={form.amount} onChange={(e) => setForm({ ...form, amount: e.target.value })} />
            <Button variant="contained" type="submit">Deposit</Button>
            <Button component={Link} to="/dashboard" variant="outlined">Back</Button>
          </Stack>
        </form>
        {message && <Typography mt={2}>{message}</Typography>}
      </CardContent>
    </Card>
  );
};

export default DepositPage;
