import { useState } from 'react';
import { Link } from 'react-router-dom';
import { Button, Card, CardContent, Stack, TextField, Typography } from '@mui/material';

const TransferPage = () => {
  const [form, setForm] = useState({ account_id: '', target: '', amount: '' });
  return (
    <Card sx={{ maxWidth: 520, mx: 'auto', mt: 6 }}>
      <CardContent>
        <Typography variant="h4" gutterBottom>Transfer Money</Typography>
        <Stack spacing={2}>
          <TextField label="From Account ID" value={form.account_id} onChange={(e) => setForm({ ...form, account_id: e.target.value })} />
          <TextField label="Recipient Account" value={form.target} onChange={(e) => setForm({ ...form, target: e.target.value })} />
          <TextField label="Amount" value={form.amount} onChange={(e) => setForm({ ...form, amount: e.target.value })} />
          <Button variant="contained">Submit</Button>
          <Button component={Link} to="/dashboard" variant="outlined">Back</Button>
        </Stack>
      </CardContent>
    </Card>
  );
};

export default TransferPage;
