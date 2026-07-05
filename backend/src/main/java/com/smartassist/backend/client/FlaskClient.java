package com.smartassist.backend.client;

import com.smartassist.backend.dto.AnalyzeRequest;
import com.smartassist.backend.dto.AnalyzeResponse;
import org.springframework.http.*;
import org.springframework.stereotype.Component;
import org.springframework.web.client.RestTemplate;

@Component
public class FlaskClient {

    private final RestTemplate restTemplate = new RestTemplate();

    private static final String FLASK_URL = "http://localhost:5000/analyze";

    public AnalyzeResponse analyze(AnalyzeRequest request) {

        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);

        HttpEntity<AnalyzeRequest> entity =
                new HttpEntity<>(request, headers);

        ResponseEntity<AnalyzeResponse> response =
                restTemplate.exchange(
                        FLASK_URL,
                        HttpMethod.POST,
                        entity,
                        AnalyzeResponse.class
                );

        return response.getBody();
    }
}