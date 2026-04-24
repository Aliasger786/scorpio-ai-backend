# Railway Deployment Guide for Aura AI Backend

## Quick Deployment Steps

### 1. Install Railway CLI
```bash
npm install -g @railway/cli
```

### 2. Login to Railway
```bash
railway login
```

### 3. Initialize Railway Project
```bash
cd /path/to/your/backend
railway init
```

### 4. Set Environment Variables
```bash
# Set required environment variables
railway variables set SECRET_KEY=your-production-secret-key-here
railway variables set DEBUG=False
railway variables set JWT_SECRET_KEY=your-jwt-secret-key-here
railway variables set CORS_ALLOWED_ORIGINS=https://your-frontend-domain.com,https://localhost:3000
railway variables set ALLOWED_HOSTS=your-app.railway.app,localhost

# Railway will automatically set DATABASE_URL for PostgreSQL
```

### 5. Deploy
```bash
railway up
```

## Environment Variables for Railway

### Required Variables
- `SECRET_KEY` - Django secret key (generate with `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`)
- `JWT_SECRET_KEY` - JWT signing key (use a different strong secret)
- `DEBUG` - Set to `False` for production
- `CORS_ALLOWED_ORIGINS` - Your frontend domains (comma-separated)
- `ALLOWED_HOSTS` - Your Railway domain and other allowed hosts

### Automatic Variables (set by Railway)
- `DATABASE_URL` - PostgreSQL connection string
- `PORT` - Port number (usually 8000)
- `RAILWAY_PUBLIC_DOMAIN` - Your app domain
- `RAILWAY_STATIC_URL` - Static files URL

## Database Configuration

Your app automatically supports:
- **Local Development**: MySQL (using DB_* variables)
- **Railway Production**: PostgreSQL (using DATABASE_URL)

No database configuration needed - Railway provides PostgreSQL automatically.

## API Endpoints After Deployment

Once deployed, your API will be available at:
- Base URL: `https://your-app.railway.app`
- Register: `POST /api/v1/auth/register/`
- Login: `POST /api/v1/auth/login/`
- Dashboard: `GET /api/v1/dashboard/stats/`
- User Profile: `GET /api/v1/auth/me/`

## Testing Your Deployment

### Test Registration
```bash
curl -X POST https://your-app.railway.app/api/v1/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{"full_name":"Test User","email":"test@example.com","password":"testpass123"}'
```

### Test Login
```bash
curl -X POST https://your-app.railway.app/api/v1/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"testpass123"}'
```

### Test Protected Endpoint
```bash
curl -X GET https://your-app.railway.app/api/v1/dashboard/stats/ \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

## Features Included

✅ **JWT Authentication** - Secure token-based auth with refresh tokens  
✅ **Password Hashing** - bcrypt for secure password storage  
✅ **CORS Support** - Configured for frontend integration  
✅ **Production Ready** - Proper security settings and logging  
✅ **Database Support** - MySQL locally, PostgreSQL on Railway  
✅ **Health Checks** - Railway automatically monitors your app  

## Troubleshooting

### Common Issues

1. **Migration Errors**
   - Railway runs migrations automatically during deployment
   - Check logs if migrations fail

2. **CORS Issues**
   - Ensure your frontend domain is in `CORS_ALLOWED_ORIGINS`
   - Include both http and https versions if needed

3. **Database Connection**
   - Railway provides PostgreSQL automatically
   - No need to set `DATABASE_URL` manually

4. **Static Files**
   - Static files are collected automatically during build
   - Served via Railway's static file hosting

### Viewing Logs
```bash
railway logs
```

### Redeploying
```bash
railway up
```

## Security Notes

- Railway automatically sets `DEBUG=False` in production
- Your app includes security middleware and headers
- JWT tokens have configurable expiration (60 minutes access, 1 day refresh)
- Passwords are hashed with bcrypt
- CORS is properly configured for frontend domains

## Next Steps

1. **Add Your Frontend** - Update `CORS_ALLOWED_ORIGINS` with your frontend URL
2. **Custom Domain** - Add a custom domain in Railway dashboard
3. **Monitor** - Check Railway dashboard for app metrics and logs
4. **Scale** - Railway automatically scales as needed
