import { BrowserRouter as Router, Routes,Route } from 'react-router-dom';
import { Header } from './components/Header';
import { HomePage } from './pages/home/Home';
import { RoomPage } from './pages/room/Room';
import { ProfilePage } from './pages/profile/Profile';
import axios from 'axios';
import { BookingPage } from './pages/booking/Booking';
import { BookingSearchPage } from './pages/booking/BookingSearch';

axios.defaults.baseURL = '/api';
axios.defaults.headers.post['Content-Type'] = 'application/json';

function App() {
  return (
    <Router>
      <Header />
      <div>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/room/:roomId" element={<RoomPage />} />
          <Route path="/booking/:bookingId" element={<BookingPage />} />
          <Route path="/booking" element={<BookingSearchPage />} />
          <Route path="/profile" element={<ProfilePage />} />
        </Routes>
      </div>
    </Router>
  )
}

export default App
