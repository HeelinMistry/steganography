import { useState } from "react";
import { Box, Button, TextField } from "@mui/material";

export default function StegForm() {
    const [carrier, setCarrier] = useState(null);
    const [payload, setPayload] = useState(null);

    const handleEncode = () => {
        console.log("Carrier:", carrier);
        console.log("Payload:", payload);
        alert("Encode clicked (backend not connected yet)");
    };

    const handleDecode = () => {
        console.log("Carrier:", carrier);
        alert("Decode clicked (backend not connected yet)");
    };

    return (
        <Box display="flex" flexDirection="column" gap={2}>
            <TextField
                type="file"
                onChange={e => setCarrier(e.target.files[0])}
                label="Carrier Image"
                InputLabelProps={{ shrink: true }}
            />
            <TextField
                type="file"
                onChange={e => setPayload(e.target.files[0])}
                label="Payload File"
                InputLabelProps={{ shrink: true }}
            />
            <Button variant="contained" onClick={handleEncode}>Encode</Button>
            <Button variant="outlined" onClick={handleDecode}>Decode</Button>
        </Box>
    );
}
