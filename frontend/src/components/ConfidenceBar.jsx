function ConfidenceBar({ value }) {
  const percent = parseFloat(value);

  return (
    <div>
      <div
        style={{
          height: 10,
          background: "#E7E5E4",
          borderRadius: 5,
          overflow: "hidden",
          marginTop: 8,
        }}
      >
        <div
          style={{
            width: percent,
            height: "100%",
            background: "#374151",
          }}
        />
      </div>

      <p
        style={{
          marginTop: 8,
        }}
      >
        {value}
      </p>
    </div>
  );
}

export default ConfidenceBar;
