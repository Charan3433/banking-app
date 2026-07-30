import { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { Button, Card, CardContent, TextField, Typography, Stack, Alert } from '@mui/material';
import axios from 'axios';

const LoginPage = () => {
  const navigate = useNavigate();
  const [form, setForm] = useState({ email: 'demo@banking.app', password: 'Password123!' });
  const [error, setError] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post('/api/auth/login', form);
      if (response.data && response.data.access_token) {
        localStorage.setItem('token', response.data.access_token);
        navigate('/dashboard');
      } else {
        setError('Login failed. No token returned.');
      }
    } catch (err) {
      const detail = err?.response?.data?.error || err?.message || 'Invalid credentials';
      setError(detail);
    }
  };

  return (
    <Card sx={{ maxWidth: 480, mx: 'auto', mt: 8 }}>
      <CardContent>
        <Typography variant="h4" gutterBottom>Banking Portal</Typography>
        <Typography color="text.secondary" mb={2}>Sign in to your secure banking dashboard</Typography>
        {error && <Alert severity="error" sx={{ mb: 2 }}>{error}</Alert>}
        <form onSubmit={handleSubmit}>
          <Stack spacing={2}>
            <TextField label="Email" value={form.email} onChange={(e) => setForm({ ...form, email: e.target.value })} fullWidth />
            <TextField label="Password" type="password" value={form.password} onChange={(e) => setForm({ ...form, password: e.target.value })} fullWidth />
            <Button variant="contained" type="submit">Login</Button>
          </Stack>
        </form>
        <Typography mt={2}>
          No account? <Link to="/register">Create one</Link>
        </Typography>
      </CardContent>
    </Card>
  );
};

export default LoginPage;
