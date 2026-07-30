import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { Button, Card, CardContent, Stack, TextField, Typography } from '@mui/material';
import axios from 'axios';

const ProfilePage = () => {
  const [user, setUser] = useState({ full_name: '', phone: '', address: '' });

  useEffect(() => {
    const fetchUser = async () => {
      const token = localStorage.getItem('token');
      const res = await axios.get('/api/users/profile', { headers: { Authorization: `Bearer ${token}` } });
      setUser(res.data.user);
    };
    fetchUser();
  }, []);

  return (
    <Card sx={{ maxWidth: 520, mx: 'auto', mt: 6 }}>
      <CardContent>
        <Typography variant="h4" gutterBottom>Profile</Typography>
        <Stack spacing={2}>
          <TextField label="Full Name" value={user.full_name || ''} onChange={(e) => setUser({ ...user, full_name: e.target.value })} />
          <TextField label="Phone" value={user.phone || ''} onChange={(e) => setUser({ ...user, phone: e.target.value })} />
          <TextField label="Address" value={user.address || ''} onChange={(e) => setUser({ ...user, address: e.target.value })} />
          <Button variant="contained">Save</Button>
          <Button component={Link} to="/dashboard" variant="outlined">Back</Button>
        </Stack>
      </CardContent>
    </Card>
  );
};

export default ProfilePage;
