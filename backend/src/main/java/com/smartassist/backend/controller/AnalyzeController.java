package com.smartassist.backend.controller;

import com.smartassist.backend.dto.AnalyzeRequest;
import com.smartassist.backend.dto.AnalyzeResponse;
import com.smartassist.backend.service.AnalyzeService;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api")
@CrossOrigin(origins = "http://localhost:5173")
public class AnalyzeController {

    private final AnalyzeService analyzeService;

    public AnalyzeController(AnalyzeService analyzeService) {
        this.analyzeService = analyzeService;
    }

    @PostMapping("/analyze")
    public AnalyzeResponse analyze(@RequestBody AnalyzeRequest request) {
        return analyzeService.analyzeTicket(request);
    }
}