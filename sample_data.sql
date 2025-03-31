INSERT INTO apps (app_name, version, description)
SELECT 'YouTube', '18.0', 'Video Streaming App'
WHERE NOT EXISTS (SELECT 1 FROM apps WHERE app_name = 'YouTube');

INSERT INTO apps (app_name, version, description)
SELECT 'WhatsApp', '2.23.8', 'Messaging App'
WHERE NOT EXISTS (SELECT 1 FROM apps WHERE app_name = 'WhatsApp');

INSERT INTO apps (app_name, version, description)
SELECT 'Instagram', '300.0', 'Social Media App'
WHERE NOT EXISTS (SELECT 1 FROM apps WHERE app_name = 'Instagram');

INSERT INTO apps (app_name, version, description)
SELECT 'Spotify', '8.7.92', 'Music Streaming App'
WHERE NOT EXISTS (SELECT 1 FROM apps WHERE app_name = 'Spotify');

INSERT INTO apps (app_name, version, description)
SELECT 'Netflix', '10.0', 'Movie & TV Streaming App'
WHERE NOT EXISTS (SELECT 1 FROM apps WHERE app_name = 'Netflix');
