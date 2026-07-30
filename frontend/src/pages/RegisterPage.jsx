import { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { Button, Card, CardContent, TextField, Typography, Stack, Alert } from '@mui/material';
import axios from 'axios';

const RegisterPage = () => {
  const navigate = useNavigate();
  const [form, setForm] = useState({ full_name: '', email: '', password: '', phone: '', address: '' });
  const [message, setMessage] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      await axios.post('/api/auth/register', form);
      setMessage('Registration successful. You can sign in.');
      setTimeout(() => navigate('/login'), 800);
    } catch (err) {
      setMessage('Registration failed');
    }
  };

  return (
    <Card sx={{ maxWidth: 560, mx: 'auto', mt: 6 }}>
      <CardContent>
        <Typography variant="h4" gutterBottom>Register</Typography>
        {message && <Alert severity="success" sx={{ mb: 2 }}>{message}</Alert>}
        <form onSubmit={handleSubmit}>
          <Stack spacing={2}>
            <TextField label="Full Name" value={form.full_name} onChange={(e) => setForm({ ...form, full_name: e.target.value })} fullWidth />
            <TextField label="Email" value={form.email} onChange={(e) => setForm({ ...form, email: e.target.value })} fullWidth />
            <TextField label="Password" type="password" value={form.password} onChange={(e) => setForm({ ...form, password: e.target.value })} fullWidth />
            <TextField label="Phone" value={form.phone} onChange={(e) => setForm({ ...form, phone: e.target.value })} fullWidth />
            <TextField label="Address" value={form.address} onChange={(e) => setForm({ ...form, address: e.target.value })} fullWidth />
            <Button variant="contained" type="submit">Register</Button>
          </Stack>
        </form>
        <Typography mt={2}><Link to="/login">Back to login</Link></Typography>
      </CardContent>
    </Card>
  );
};

export default RegisterPage;
