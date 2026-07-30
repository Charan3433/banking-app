import { Routes, Route, Navigate } from 'react-router-dom';
import { Container, CssBaseline, ThemeProvider, createTheme } from '@mui/material';
import LoginPage from './pages/LoginPage';
import RegisterPage from './pages/RegisterPage';
import DashboardPage from './pages/DashboardPage';
import AccountsPage from './pages/AccountsPage';
import TransactionsPage from './pages/TransactionsPage';
import TransferPage from './pages/TransferPage';
import DepositPage from './pages/DepositPage';
import WithdrawPage from './pages/WithdrawPage';
import ProfilePage from './pages/ProfilePage';
import NotFoundPage from './pages/NotFoundPage';

const theme = createTheme({ palette: { mode: 'light', primary: { main: '#1e3a8a' }, secondary: { main: '#0f766e' } } });

const App = () => {
  const token = localStorage.getItem('token');

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Container maxWidth="lg" sx={{ py: 4 }}>
        <Routes>
          <Route path="/" element={token ? <Navigate to="/dashboard" replace /> : <LoginPage />} />
          <Route path="/login" element={token ? <Navigate to="/dashboard" replace /> : <LoginPage />} />
          <Route path="/register" element={token ? <Navigate to="/dashboard" replace /> : <RegisterPage />} />
          <Route path="/dashboard" element={token ? <DashboardPage /> : <Navigate to="/login" replace />} />
          <Route path="/accounts" element={token ? <AccountsPage /> : <Navigate to="/login" replace />} />
          <Route path="/transactions" element={token ? <TransactionsPage /> : <Navigate to="/login" replace />} />
          <Route path="/transfer" element={token ? <TransferPage /> : <Navigate to="/login" replace />} />
          <Route path="/deposit" element={token ? <DepositPage /> : <Navigate to="/login" replace />} />
          <Route path="/withdraw" element={token ? <WithdrawPage /> : <Navigate to="/login" replace />} />
          <Route path="/profile" element={token ? <ProfilePage /> : <Navigate to="/login" replace />} />
          <Route path="*" element={<NotFoundPage />} />
        </Routes>
      </Container>
    </ThemeProvider>
  );
};

export default App;
