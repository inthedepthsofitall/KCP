import axios from 'axios';
import { useState } from 'react';

const backendUrl = process.env.REACT_APP_API_URL + '/urls/'; 

function URLShortener() {
    const [url, setUrl] = useState('');
    const [shortUrl, setShortUrl] = useState('');

    const handleSubmit = async (event) => {
        event.preventDefault();
        const config = {
            headers: {
                'Content-Type': 'application/json'
            }
        };
        try {
            const response = await axios.post(backendUrl, JSON.stringify({ original_url: url }), config);
            setShortUrl(response.data.short_url);
            console.log(response.data);
        } catch (error) {
            console.error('Error:', error.response ? error.response.data : error.message);
        }
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <input type="text" value={url} onChange={e => setUrl(e.target.value)} placeholder="Enter URL here" />
                <button type="submit">Shorten URL</button>
            </form>
            {shortUrl && <p>Short URL: <a href={`${process.env.REACT_APP_API_URL}/r/${shortUrl}`}>{shortUrl}</a></p>}
        </div>
    );
}

export default URLShortener;
