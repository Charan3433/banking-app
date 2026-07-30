import { Link } from 'react-router-dom';
import { Button, Card, CardContent, Typography } from '@mui/material';

const NotFoundPage = () => (
  <Card sx={{ maxWidth: 480, mx: 'auto', mt: 10 }}>
    <CardContent>
      <Typography variant="h4" gutterBottom>404</Typography>
      <Typography color="text.secondary">The page you are looking for does not exist.</Typography>
      <Button component={Link} to="/" variant="contained" sx={{ mt: 2 }}>Go Home</Button>
    </CardContent>
  </Card>
);

export default NotFoundPage;
