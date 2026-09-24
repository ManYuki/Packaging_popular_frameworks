package com.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.beans.factory.annotation.Value;
import java.util.Map;

@SpringBootApplication
@RestController
public class DemoApplication {

    @Value("${APP_MESSAGE:Default Spring Boot Config}")
    private String message;

    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }

    @GetMapping("/")
    public Map<String, String> home() {
        return Map.of(
            "status", "active",
            "message", message,
            "framework", "Spring Boot"
        );
    }
}
