import React from 'react';
import { Button, Container } from 'react-bootstrap';
import './Home.css';

const Home: React.FC = () => {
    return (
        <Container className='home-container'>
            <div className='home-wrapper'>
                <Button href="/legislators" size='lg'>Legislators</Button>
                <Button href="/bills" size='lg'>Bills</Button>
            </div>
        </Container>
    );
}

export default Home;