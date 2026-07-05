package com.smartassist.backend.dto;

import lombok.Data;

@Data
public class AnalyzeResponse {

    private String summary;

    private String sentiment;

    private String sentimentConfidence;

    private String recommendedDepartment;

    private String recommendedPriority;

    private String suggestedResolution;

    private String draftReply;

    private String confidence;

}