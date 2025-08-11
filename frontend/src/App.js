import { useState, useMemo } from "react";
import { ThemeProvider, createTheme, CssBaseline, Button, Container, Typography, Box } from "@mui/material";
import StegForm from "./StegForm";

export default function App() {
    const [mode, setMode] = useState("light");

    const theme = useMemo(() =>
        createTheme({
            palette: {
                mode,
                primary: { main: mode === "light" ? "#1976d2" : "#90caf9" },
                background: { default: mode === "light" ? "#f5f5f5" : "#121212" }
            },
        }), [mode]);

    return (
        <ThemeProvider theme={theme}>
            <CssBaseline />
            <Container maxWidth="sm" sx={{ py: 4 }}>
                <Box display="flex" justifyContent="space-between" alignItems="center" mb={3}>
                    <Typography variant="h5">Steganography Tool</Typography>
                    <Button variant="outlined" onClick={() => setMode(prev => prev === "light" ? "dark" : "light")}>
                        {mode === "light" ? "Dark Mode" : "Light Mode"}
                    </Button>
                </Box>
                <StegForm />
            </Container>
        </ThemeProvider>
    );
}
