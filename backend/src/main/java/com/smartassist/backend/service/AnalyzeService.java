package com.smartassist.backend.service;

import com.smartassist.backend.client.FlaskClient;
import com.smartassist.backend.dto.AnalyzeRequest;
import com.smartassist.backend.dto.AnalyzeResponse;
import org.springframework.stereotype.Service;

@Service
public class AnalyzeService {

    private final FlaskClient flaskClient;

    public AnalyzeService(FlaskClient flaskClient) {
        this.flaskClient = flaskClient;
    }

    public AnalyzeResponse analyzeTicket(AnalyzeRequest request) {
        return flaskClient.analyze(request);
    }
}